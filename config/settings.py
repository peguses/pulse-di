import os
from dotenv import load_dotenv

from models.db_settings import DbSettings
from models.auth_settings import AuthSettings


def load_env_file():
    env_file = os.getenv("ENV_FILE", ".env")
    load_dotenv(env_file)
    print(f"Loaded environment variables from {env_file}")


load_env_file()

db_settings = DbSettings(
    mongo_db_url=str(os.getenv("MONGODB_URI")),
    mongo_db=str(os.getenv("MONGODB_DB_NAME")),
)

# auth_settings = AuthSettings(
#     jwt_access_token_expire_minutes=str(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES")),
#     jwt_algorithm=str(os.getenv("JWT_ALGORITHM")),
#     jwt_secret_key=str(os.getenv("JWT_SECRET_KEY")),
# )

google_auth_settings = AuthSettings(
    client_id=str(os.getenv("GOOGLE_CLIENT_ID")),
    client_secret=str(os.getenv("GOOGLE_CLIENT_SECRET")),
    redirect_url=str(os.getenv("GOOGLE_REDIRECT_URL")),
    authorize_url=str(os.getenv("GOOGLE_AUTHORIZE_URL")),
    access_token_url=str(os.getenv("GOOGLE_ACCESS_TOKEN_URL")),
    profile_info_url=str(os.getenv("GOOGLE_PROFILE_INFO_URL")),
    jwks_uri=str(os.getenv("GOOGLE_JWKS_URI")),
)


facebook_auth_settings = AuthSettings(
    client_id=str(os.getenv("FACEBOOK_CLIENT_ID")),
    client_secret=str(os.getenv("FACEBOOK_CLIENT_SECRET")),
    redirect_url=str(os.getenv("FACEBOOK_REDIRECT_URL")),
    authorize_url=str(os.getenv("FACEBOOK_AUTHORIZE_URL")),
    access_token_url=str(os.getenv("FACEBOOK_ACCESS_TOKEN_URL")),
    profile_info_url=str(os.getenv("FACEBOOK_PROFILE_INFO_URL")),
    jwks_uri=str(os.getenv("FACEBOOK_JWKS_URI")),
)
