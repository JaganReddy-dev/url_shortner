from shortener_app.Data.db.mongo_client import api_keys_collection
from shortener_app.Utils.api_keys.api_key_gen import api_key_generator
from shortener_app.Utils.api_keys.hashed.hash import hash
import uuid


def create_api_key_service(user_uuid: str, name: str) -> str:
    data = api_key_generator()
    hashed_api_key = hash(data.get("api_key"))
    new_uuid = uuid.uuid4()
    object = {
        {
            "id": new_uuid,
            "name": name,
            "api_key_hash": hashed_api_key,
            "created_at": data.get("created_at"),
            "expires_at": data.get("expires_at"),
            "user_id": user_uuid,
            "is_active": True,
        }
    }
    api_keys_collection.insert_one(object)
    return object
