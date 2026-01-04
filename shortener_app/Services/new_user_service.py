import uuid
from datetime import datetime, timezone
from shortener_app.Data.db.mongo_client import url_map_collection
from pymongo import ReturnDocument

dt = datetime.timestamp


def new_user_service(user_name: str) -> dict:
    now = datetime.now(timezone.utc)

    user_data = {
        "user_id": str(uuid.uuid4()),
        "user_name": user_name,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }

    url_map_collection.insert_one(user_data)
    return user_data


def update_user_service(user_name: str, new_user_name: str) -> dict | None:
    updated_at = datetime.now(timezone.utc)

    result = url_map_collection.find_one_and_update(
        {"user_name": user_name},
        {
            "$set": {
                "user_name": new_user_name,
                "updated_at": updated_at,
            }
        },
        return_document=ReturnDocument.AFTER,
    )

    return result
