import strawberry

from admin.models.user import PaginatedUserType
from admin.schemas.user import deserialize_users
from config.database import user_collection
from models.pagination import PaginationInfo


@strawberry.type
class UserQuery:

    @strawberry.field
    async def get_users(self, limit: int, page: int = 0) -> PaginatedUserType:

        total_count = await user_collection.count_documents({})
        total_pages = (total_count + limit - 1) // limit

        users_cursor = user_collection.find({}).skip(page * limit).limit(limit)
        users = await users_cursor.to_list(length=limit)

        pagination_info = PaginationInfo(
            page=page, page_size=limit, total_pages=total_pages, total_count=total_count
        )

        return PaginatedUserType(
            users=deserialize_users(users), pagination=pagination_info
        )
