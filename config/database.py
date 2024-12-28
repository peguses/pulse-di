from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://admin:admin@localhost:27017")

db = client.pulse_di

user_collection = db["users"]

user_collection.create_index([("email", 1)], unique=True)

role_collection = db["roles"]
