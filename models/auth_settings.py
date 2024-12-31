from pydantic import BaseModel


class AuthSettings(BaseModel):
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_token_expire_minutes: str
