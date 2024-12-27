import strawberry

from admin.models.user import User
from admin.models.user_input import UserInput
from admin.schemas.user import deserialize_user, serialize_user
from config.database import user_collection


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_user(self, user: UserInput) -> User:
        user_data = serialize_user(user)
        result = await user_collection.insert_one(user_data)
        return deserialize_user(
            await user_collection.find_one({"_id": result.inserted_id})
        )
