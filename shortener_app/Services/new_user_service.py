from datetime import datetime, timezone
from fastapi import HTTPException
from pymongo import ReturnDocument
from pymongo.errors import DuplicateKeyError
from shortener_app.Data.DB.mongo_client import users_collection


def new_user_service(user_name: str) -> dict:
    user_name = user_name.strip().lower()
    now = datetime.now(timezone.utc)

    user_data = {
        "user_name": user_name,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }

    try:
        result = users_collection.insert_one(user_data)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="User already exists")
    return {
        "id": str(result.inserted_id),
        "user_name": user_data["user_name"],
        "is_active": user_data["is_active"],
        "created_at": user_data["created_at"],
        "updated_at": user_data["updated_at"],
    }


def update_user_service(user_name: str, new_user_name: str) -> dict:
    user_name = user_name.strip().lower()
    new_user_name = new_user_name.strip().lower()
    updated_at = datetime.now(timezone.utc)

    try:
        result = users_collection.find_one_and_update(
            {"user_name": user_name},
            {
                "$set": {
                    "user_name": new_user_name,
                    "updated_at": updated_at,
                }
            },
            return_document=ReturnDocument.AFTER,
        )
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="New user name already exists")

    if not result:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": str(result["_id"]),
        "user_name": result["user_name"],
        "is_active": result["is_active"],
        "updated_at": result["updated_at"],
    }
