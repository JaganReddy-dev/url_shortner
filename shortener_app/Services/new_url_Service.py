from shortener_app.Data.DB.mongo_client import url_map_collection
from shortener_app.Data.DB.mongo_client import api_keys_collection
from shortener_app.Data.DB.mongo_client import counter_collection
from shortener_app.Utils.urls.path_encrypt.base62_encode import encode_base62
from shortener_app.Utils.urls.path_encrypt.obfuscate import obfuscate_counter
from shortener_app.Utils.api_keys.hashed.hash import hash
from pymongo import ReturnDocument
from pymongo.errors import DuplicateKeyError
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException


async def create_new_short_url_service(long_url: str, api_key: str) -> dict:
    """
    Creates a new short URL for the given long URL.

    Args:
        long_url: The original URL to shorten
        api_key: User's API key for authentication

    Returns:
        dict: Created short URL details

    Raises:
        HTTPException: 400 if params missing, 401 if invalid API key,
                      409 if URL already exists
    """
    if not long_url or not api_key:
        raise HTTPException(status_code=400, detail="Long URL and API key are required")

    # Hash and validate API key
    hashed_api_key = hash(api_key)
    api_key_doc = await api_keys_collection.find_one(
        {"api_key_hash": hashed_api_key, "is_active": True}
    )

    if not api_key_doc:
        raise HTTPException(status_code=401, detail="Invalid or inactive API key")

    user_uuid = api_key_doc["user_id"]

    # Check if URL already exists for this user
    existing = await url_map_collection.find_one(
        {
            "user_id": user_uuid,
            "long_url": long_url,
        }
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail=f"Short URL already exists: {existing['short_url_path']}",
        )

    # Get next counter value
    count_doc = await counter_collection.find_one_and_update(
        {"_id": "url_counter"},
        {"$inc": {"count": 1}},
        upsert=True,
        return_document=ReturnDocument.AFTER,
    )
    count = count_doc["count"]

    # Generate short URL path
    obfuscated_counter_value = obfuscate_counter(count)
    short_url_path = encode_base62(obfuscated_counter_value)

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
        result = await url_map_collection.insert_one(doc)
    except DuplicateKeyError:
        # Rare case: short_url_path collision
        raise HTTPException(
            status_code=500, detail="Short URL generation collision. Please retry."
        )

    return {
        "id": str(result.inserted_id),
        "long_url": long_url,
        "short_url_path": short_url_path,
        "created_at": created_at,
        "expires_at": expires_at,
        "user_id": user_uuid,
        "is_active": True,
    }
