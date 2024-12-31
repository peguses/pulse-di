from pydantic import BaseModel


class GoogleAuthSettings(BaseModel):
    google_client_id: str
    google_client_secret: str
    google_redirect_url: str
    google_authorize_url: str
    google_access_token_url: str
    google_profile_info_url: str
    google_jwks_uri: str
