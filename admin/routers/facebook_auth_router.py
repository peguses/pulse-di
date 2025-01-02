from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from admin.auth.facebook_auth import FacebookAuth
from admin.enums.auth_provider import AuthProvider
from config.settings import facebook_auth_settings


facebook_auth_router = APIRouter()

facebook_auth = FacebookAuth()


@facebook_auth_router.get("/facebook_login")
async def login(request: Request):
    return await facebook_auth.authorize_redirect(
        request, facebook_auth_settings.redirect_url
    )


@facebook_auth_router.get("/facebook_callback")
async def callback(request: Request):
    token = await facebook_auth.auth.authorize_access_token(request)

    first_name, last_name, email = await facebook_auth.get_user_profile(
        facebook_auth_settings.profile_info_url, token["access_token"]
    )

    await facebook_auth.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        auth_provider=AuthProvider.FACEBOOK,
    )

    response = RedirectResponse(url="/graphql")
    return response
