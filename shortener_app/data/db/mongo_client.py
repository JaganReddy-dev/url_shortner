from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("DB_URI")

# Create async client and connect to the server
client = AsyncMongoClient(uri, server_api=ServerApi("1"))

db = client["url_shortener"]
api_keys_collection = db["api_keys"]
url_map_collection = db["url_map"]
users_collection = db["users"]
counter_collection = db["counter"]
user_collection = db["user"]
roles_collection = db["roles"]


async def initialize_database():
    """
    Initialize database connection and create indexes.
    Call this function on application startup.
    """
    # Test connection
    try:
        await client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(f"MongoDB connection error: {e}")
        raise

    # Create indexes
    await users_collection.create_index("user_name", unique=True)
    await url_map_collection.create_index(
        [("user_id", 1), ("short_url_path", 1)], unique=True
    )
    await url_map_collection.create_index("expires_at", expireAfterSeconds=0)
    await api_keys_collection.create_index("api_key_hash", unique=True)
    await api_keys_collection.create_index("expires_at", expireAfterSeconds=0)

    print("Database indexes created successfully!")


async def close_database():
    """
    Close database connection.
    Call this function on application shutdown.
    """
    client.close()
    print("MongoDB connection closed.")
