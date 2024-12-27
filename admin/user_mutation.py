import strawberry

from admin.models.user_type import UserType
from admin.models.user_input import UserInput
from admin.schemas.user import deserialize_user, serialize_user
from config.database import user_collection


@strawberry.type
class UserMutation:

    @strawberry.mutation
    async def create_user(self, user: UserInput) -> UserType:
        user_data = serialize_user(user)
        result = await user_collection.insert_one(user_data)
        return deserialize_user(
            await user_collection.find_one({"_id": result.inserted_id})
        )
