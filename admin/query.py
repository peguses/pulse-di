from typing import List
import strawberry

from admin.models.user_type import UserType
from admin.schemas.user import deserialize_users
from config.database import user_collection


@strawberry.type
class Query:

    @strawberry.field
    async def users(self) -> List[UserType]:
        for users in user_collection.find():
            return deserialize_users(users)
