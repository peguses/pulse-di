from abc import ABC, abstractmethod
from fastapi import Request
from pymongo.errors import DuplicateKeyError
from admin.enums.auth_provider import AuthProvider
from admin.enums.roles import Roles
from admin.exceptions.DuplicateEmailException import DuplicateEmailException
from admin.exceptions.NotFoundException import NotFoundException
from admin.models.permission import PermissionInput
from admin.models.role import RoleInputRequest
from admin.models.user import UserInputRequest
from admin.schemas.user import validate_and_serialize_user
from config.database import role_collection, user_collection


class Auth(ABC):

    @property
    def auth(self):
        pass

    @auth.setter
    def auth(self, value):
        self._auth = value

    @auth.getter
    def auth(self):
        return self._auth

    @abstractmethod
    async def authorize_redirect(self, request: Request, redirect_url: str):
        pass

    @abstractmethod
    async def get_user_profile(self, profile_info_url: str, token: str):
        pass

    async def create_user(
        self, first_name, last_name, email, auth_provider: AuthProvider
    ):
        role = await role_collection.find_one({"role": Roles.GUEST.name})

        if not role:
            raise NotFoundException("Guest role not found")

        user = UserInputRequest(
            id=None,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password="1qaz2wsxW@",
            auth_provider=auth_provider,
            role=RoleInputRequest(
                name=role["name"],
                role=role["role"],
                permissions=[
                    PermissionInput(
                        subject=permission["subject"], actions=permission["actions"]
                    )
                    for permission in role["permissions"]
                ],
            ),
        )

        try:

            await user_collection.insert_one(validate_and_serialize_user(user))

        except DuplicateKeyError as de:
            raise DuplicateEmailException(
                f"The email {user.email} is already in use."
            ) from de
