from shortener_app.Data.DB.mongo_client import api_keys_collection
from shortener_app.Utils.api_keys.api_key_gen import api_key_generator
from shortener_app.Utils.api_keys.hashed.hash import hash_api_key
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException


async def create_api_key_service(user_uuid: str, name: str) -> dict:
    """
    Creates a new API key for a user.

    Args:
        user_uuid: The user's UUID
        name: Name/label for the API key

    Returns:
        dict: API key details including the plaintext key (only shown once)

    Raises:
        HTTPException: 409 if API key with same name already exists for user
    """
    # Generate API key and metadata
    data = api_key_generator()
    hashed_api_key = hash_api_key(data["api_key"])

    document = {
        "name": name,
        "api_key_hash": hashed_api_key,
        "created_at": data["created_at"],
        "expires_at": data["expires_at"],
        "user_id": user_uuid,
        "is_active": True,
    }

    try:
        result = await api_keys_collection.insert_one(document)
    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail=f"API key with name '{name}' already exists"
        )

    return {
        "id": str(result.inserted_id),
        "name": name,
        "api_key": data["api_key"],  # Plaintext key - only returned once!
        "created_at": data["created_at"],
        "expires_at": data["expires_at"],
        "user_id": user_uuid,
        "is_active": True,
    }
