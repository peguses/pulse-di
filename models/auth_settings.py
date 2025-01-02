from pydantic import BaseModel


class AuthSettings(BaseModel):
    client_id: str
    client_secret: str
    redirect_url: str
    authorize_url: str
    access_token_url: str
    profile_info_url: str
    jwks_uri: str
