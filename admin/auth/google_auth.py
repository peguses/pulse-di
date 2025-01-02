from authlib.integrations.starlette_client import OAuth
from fastapi import Request
from pymongo.errors import DuplicateKeyError
import httpx
from admin.auth.auth import Auth
from admin.enums.roles import Roles
from admin.exceptions.DuplicateEmailException import DuplicateEmailException
from admin.exceptions.NotFoundException import NotFoundException
from admin.models.permission import PermissionInput
from admin.models.role import RoleInputRequest
from admin.models.user import UserInputRequest
from admin.schemas.user import validate_and_serialize_user
from config.settings import google_auth_settings
from config.database import role_collection, user_collection


class GoogleAuth(Auth):

    def __init__(self):
        super().__init__()
        self.auth = OAuth().register(
            "google",
            client_id=google_auth_settings.google_client_id,
            client_secret=google_auth_settings.google_client_secret,
            authorize_url=google_auth_settings.google_authorize_url,
            authorize_params=None,
            jwks_uri=google_auth_settings.google_jwks_uri,
            access_token_url=google_auth_settings.google_access_token_url,
            refresh_token_url=None,
            client_kwargs={"scope": "openid email profile"},
        )

    async def authorize_redirect(self, request: Request, redirect_url):
        return await self._auth.authorize_redirect(request, redirect_url)

    async def get_google_user_profile(self, profile_info_url: str, token: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                google_auth_settings.google_profile_info_url,
                headers={"Authorization": f"Bearer {token}"},
            )

            if response.status_code == 200:
                user_info = response.json()
                first_name = user_info.get("given_name", "Unknown")
                last_name = user_info.get("family_name", "Unknown")
                email = user_info.get("email", "Unknown")
                return first_name, last_name, email
            else:
                raise ValueError("Failed to fetch user profile information")

    async def create_user(self, first_name, last_name, email):
        role = await role_collection.find_one({"role": Roles.GUEST.name})

        if not role:
            raise NotFoundException("Guest role not found")

        user = UserInputRequest(
            id=None,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password="1qaz2wsxW@",
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
