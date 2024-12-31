from pydantic import BaseModel


class DbSettings(BaseModel):
    mongo_db_url: str
    mongo_db: str
