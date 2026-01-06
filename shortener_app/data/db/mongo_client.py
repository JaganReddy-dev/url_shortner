from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("DB_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["url_shortener"]
api_keys_collection = db["api_keys"]
url_map_collection = db["url_map"]
users_collection = db["users"]
counter_collection = db["counter"]

users_collection.create_index("user_name", unique=True)
url_map_collection.create_index([("user_id", 1), ("long_url", 1)], unique=True)
url_map_collection.create_index("expires_at", expireAfterSeconds=0)
api_keys_collection.create_index("api_key_hash", unique=True)
api_keys_collection.create_index("expires_at", expireAfterSeconds=0)
