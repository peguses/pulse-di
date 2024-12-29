from typing import List
import strawberry

from admin.models.user import UserType
from admin.schemas.user import deserialize_users
from config.database import user_collection


@strawberry.type
class UserQuery:

    @strawberry.field
    async def get_users(self) -> List[UserType]:
        for users in user_collection.find():
            return deserialize_users(users)
