import os
from dotenv import load_dotenv

from models.settings import Settings


def load_env_file() -> Settings:
    env_file = os.getenv("ENV_FILE", ".env")
    load_dotenv(env_file)
    print(f"Loaded environment variables from {env_file}")


load_env_file()

settings = Settings(
    mongo_db_url=str(os.getenv("MONGODB_URI")),
    mongo_db=str(os.getenv("MONGODB_DB_NAME")),
    google_client_id=str(os.getenv("GOOGLE_CLIENT_ID")),
    google_client_secret=str(os.getenv("GOOGLE_CLIENT_SECRET")),
    google_redirect_url=str(os.getenv("GOOGLE_REDIRECT_URI")),
    jwt_access_token_expire_minutes=str(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES")),
    jwt_algorithm=str(os.getenv("JWT_ALGORITHM")),
    jwt_secret_key=str(os.getenv("JWT_SECRET_KEY")),
)