from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from pymongo.errors import DuplicateKeyError
import httpx
from admin.auth.google_auth import google
from admin.schemas.user import validate_and_serialize_user
from config.database import role_collection, user_collection
from admin.enums.roles import Roles
from admin.exceptions.NotFoundException import NotFoundException
from admin.exceptions.DuplicateEmailException import DuplicateEmailException
from admin.models.role import RoleInputRequest
from admin.models.user import UserInputRequest
from config.settings import google_auth_settings

auth_router = APIRouter()


@auth_router.get("/login")
async def login(request: Request):
    return await google.authorize_redirect(
        request, google_auth_settings.google_redirect_url
    )


@auth_router.get("/callback")
async def callback(request: Request):
    token = await google.authorize_access_token(request)
    first_name, last_name, email = await get_google_user_profile(token["access_token"])

    role = await role_collection.find_one({"role": Roles.GUEST.name})

    if not role:
        raise NotFoundException("Guest role not found")

    print(role)
    user = UserInputRequest(
        id=None,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password="1qaz2wsxW@",
        role=RoleInputRequest(
            name=role["name"], role=role["role"], permissions=PermissionInput
        ),
    )

    try:

        user_collection.insert_one(validate_and_serialize_user(user))

    except DuplicateKeyError as de:
        raise DuplicateEmailException(
            f"The email {user.email} is already in use."
        ) from de

    response = RedirectResponse(url="/graphql")
    return response


async def get_google_user_profile(token: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            google_auth_settings.google_profile_info_url,
            headers={"Authorization": f"Bearer {token}"},
        )

        if response.status_code == 200:
            user_info = response.json()
            print(user_info)
            first_name = user_info.get("given_name", "Unknown")
            last_name = user_info.get("family_name", "Unknown")
            email = user_info.get("email", "Unknown")
            return first_name, last_name, email
        else:
            raise ValueError("Failed to fetch user profile information")
