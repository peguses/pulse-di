from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from admin.auth.google_auth import GoogleAuth
from config.settings import google_auth_settings

auth_router = APIRouter()

google_auth = GoogleAuth()


@auth_router.get("/login")
async def login(request: Request):
    return await google_auth.authorize_redirect(
        request, google_auth_settings.redirect_url
    )


@auth_router.get("/callback")
async def callback(request: Request):
    print(google_auth.auth)
    token = await google_auth.auth.authorize_access_token(request)
    first_name, last_name, email = await google_auth.get_user_profile(
        google_auth_settings.profile_info_url, token["access_token"]
    )

    await google_auth.create_user(
        first_name=first_name, last_name=last_name, email=email
    )

    response = RedirectResponse(url="/graphql")
    return response
