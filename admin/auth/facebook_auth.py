from authlib.integrations.starlette_client import OAuth
from fastapi import Request
from admin.auth.auth import Auth
from config.settings import facebook_auth_settings


class FacebookAuth(Auth):
    def __init__(self):
        super().__init__()
        self.auth = OAuth().register(
            "google",
            client_id=facebook_auth_settings.client_id,
            client_secret=facebook_auth_settings.client_secret,
            authorize_url=facebook_auth_settings.authorize_url,
            authorize_params=None,
            jwks_uri=facebook_auth_settings.jwks_uri,
            access_token_url=facebook_auth_settings.access_token_url,
            refresh_token_url=None,
            client_kwargs={"scope": "openid email profile"},
        )

    async def authorize_redirect(self, request: Request, redirect_url):
        return await self._auth.authorize_redirect(request, redirect_url)

    async def get_user_profile(self, profile_info_url: str, token: str):
        pass

    async def create_user(self, first_name, last_name, email):
        pass
