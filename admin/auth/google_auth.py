from authlib.integrations.starlette_client import OAuth

from config.settings import google_auth_settings

oauth = OAuth()

google = oauth.register(
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
