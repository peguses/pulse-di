from pydantic import BaseModel


class Settings(BaseModel):
    mongo_db_url: str
    mongo_db: str
    google_client_id: str
    google_client_secret: str
    google_redirect_url: str
    google_authorize_url: str
    google_access_token_url: str
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_token_expire_minutes: str
