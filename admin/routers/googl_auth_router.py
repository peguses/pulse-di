from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from admin.auth.google_auth import GoogleAuth
from admin.enums.auth_provider import AuthProvider
from config.settings import google_auth_settings

google_auth_router = APIRouter()

google_auth = GoogleAuth()


@google_auth_router.get("/google_login")
async def login(request: Request):
    return await google_auth.authorize_redirect(
        request, google_auth_settings.redirect_url
    )


@google_auth_router.get("/google_callback")
async def callback(request: Request):
    token = await google_auth.auth.authorize_access_token(request)
    first_name, last_name, email = await google_auth.get_user_profile(
        google_auth_settings.profile_info_url, token["access_token"]
    )

    await google_auth.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        auth_provider=AuthProvider.GOOGLE,
    )

    response = RedirectResponse(url="/graphql")
    return response
