from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://admin:admin@localhost:27017")

db = client.pulse_di

user_collection = db["users"]
