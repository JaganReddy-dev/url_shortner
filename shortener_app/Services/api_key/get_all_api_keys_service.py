from shortener_app.Data.DB.mongo_client import api_keys_collection
from shortener_app.Utils.api_keys.hashed.hash import hash_api_key


async def get_all_api_keys_service(user_uuid: str):
    """Retrieve all API keys associated with a given user UUID."""
    api_keys_cursor = api_keys_collection.find({"user_uuid": user_uuid})
    api_keys = []
    async for api_key in api_keys_cursor:
        api_key_hash = api_key["api_key_hash"]
        api_keys.append(hash_api_key(api_key_hash))
