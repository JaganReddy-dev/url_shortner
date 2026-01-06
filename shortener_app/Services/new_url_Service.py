from shortener_app.Data.DB.mongo_client import url_map_collection
from shortener_app.Data.DB.mongo_client import api_keys_collection
from shortener_app.Utils.urls.path_encrypt.base62_encode import encode_base62
from shortener_app.Utils.urls.path_encrypt.obfuscate import obfuscate_counter
from shortener_app.Utils.api_keys.hashed.hash import hash
from shortener_app.Data.DB.mongo_client import counter_collection
from pymongo import ReturnDocument
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError


def create_new_short_url_service(long_url: str, api_key: str) -> str:
    if not long_url or not api_key:
        raise HTTPException(status_code=400, detail="Long URL and API key are required")

    # Hash API key
    hashed_api_key = hash(api_key)

    # Validate API key and get user UUID
    api_key_doc = api_keys_collection.find_one(
        {"api_key_hash": hashed_api_key, "is_active": True}
    )
    if not api_key_doc:
        raise HTTPException(status_code=401, detail="Invalid or inactive API key")

    user_uuid = api_key_doc["user_id"]

    existing = url_map_collection.find_one(
        {
            "user_id": user_uuid,
            "long_url": long_url,
        }
    )

    if existing:
        if existing["is_active"]:
            return {
                "id": str(existing["_id"]),
                "short_url_path": existing["short_url_path"],
                "status": "already_active",
            }
        else:
            url_map_collection.update_one(
                {"_id": existing["_id"]}, {"$set": {"is_active": True}}
            )
            return {
                "id": str(existing["_id"]),
                "short_url_path": existing["short_url_path"],
                "status": "reactivated",
            }

    # update current counter value and get the new value
    count = counter_collection.find_one_and_update(
        {"_id": "url_counter"},
        {"$inc": {"count": 1}},
        upsert=True,
        return_document=ReturnDocument.AFTER,
    )["count"]

    # create obfuscated counter value
    obfuscated_counter = obfuscate_counter(count)

    # create short url path
    short_url_path = encode_base62(obfuscated_counter)
    created_at = datetime.now(timezone.utc)
    expires_at = created_at + timedelta(days=30)

    doc = {
        "long_url": long_url,
        "short_url_path": short_url_path,
        "created_at": created_at,
        "expires_at": expires_at,
        "user_id": user_uuid,
        "is_active": True,
    }
    try:
        result = url_map_collection.insert_one(doc)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Long URL already exists")
    return {
        "id": str(result.inserted_id),
        "long_url": long_url,
        "short_url_path": short_url_path,
        "created_at": created_at,
        "expires_at": expires_at,
        "user_id": user_uuid,
        "is_active": doc.get("is_active"),
    }
