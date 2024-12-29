from authlib.integrations.starlette_client import OAuth

from config.settings import settings

oauth = OAuth()

google = oauth.register(
    "google",
    client_id=settings.google_client_id,
    client_secret=settings.google_client_secret,
    authorize_url=settings.google_authorize_url,
    authorize_params=None,
    access_token_url=settings.google_access_token_url,
    refresh_token_url=None,
    client_kwargs={"scope": "openid profile email"},
)
