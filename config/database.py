from motor.motor_asyncio import AsyncIOMotorClient

from config.settings import db_settings

client = AsyncIOMotorClient(db_settings.mongo_db_url)

db = client[db_settings.mongo_db]

user_collection = db["users"]

user_collection.create_index([("email", 1)], unique=True)

role_collection = db["roles"]
