from fastapi import APIRouter, Request
from config.settings import settings
from admin.auth.google_auth import google

auth_router = APIRouter()


@auth_router.get("/login")
async def login(request: Request):
    return await google.authorize_redirect(request, settings.google_redirect_url)
