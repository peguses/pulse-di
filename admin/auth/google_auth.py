from authlib.integrations.starlette_client import OAuth
from fastapi import Request
import httpx
from admin.auth.auth import Auth
from config.settings import google_auth_settings


class GoogleAuth(Auth):

    def __init__(self):
        super().__init__()
        self.auth = OAuth().register(
            "google",
            client_id=google_auth_settings.client_id,
            client_secret=google_auth_settings.client_secret,
            authorize_url=google_auth_settings.authorize_url,
            authorize_params=None,
            jwks_uri=google_auth_settings.jwks_uri,
            access_token_url=google_auth_settings.access_token_url,
            refresh_token_url=None,
            client_kwargs={"scope": "openid email profile"},
        )

    async def authorize_redirect(self, request: Request, redirect_url):
        return await self._auth.authorize_redirect(request, redirect_url)

    async def get_user_profile(self, profile_info_url: str, token: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                profile_info_url,
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
