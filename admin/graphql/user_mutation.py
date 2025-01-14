from typing import Optional
from pymongo.errors import DuplicateKeyError
import strawberry

from admin.enums.auth_provider import AuthProvider
from admin.exceptions.DuplicateEmailException import DuplicateEmailException
from admin.models.user import UserInputRequest, UserType
from admin.schemas.user import (
    deserialize_user,
    validate_and_serialize_user,
)
from config.database import user_collection


@strawberry.type
class UserMutation:

    @strawberry.mutation
    async def create_user(self, user: UserInputRequest) -> Optional[UserType]:
        try:
            user.auth_provider = AuthProvider.SELF
            user_data = validate_and_serialize_user(user)
            result = await user_collection.insert_one(user_data)
            return deserialize_user(
                await user_collection.find_one({"_id": result.inserted_id})
            )
        except DuplicateKeyError as de:
            raise DuplicateEmailException(
                f"The email {user.email} is already in use."
            ) from de
