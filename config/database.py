from motor.motor_asyncio import AsyncIOMotorClient

from config.settings import settings

client = AsyncIOMotorClient(settings.mongo_db_url)

db = client[settings.mongo_db]

user_collection = db["users"]

user_collection.create_index([("email", 1)], unique=True)

role_collection = db["roles"]
