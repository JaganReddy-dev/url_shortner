def individual_api_key_response(api_key_record):
    return {
        "id": str(api_key_record["_id"]),
        "name": api_key_record["name"],
        "api_key_hash": api_key_record["api_key_hash"],
        "user_id": api_key_record["user_id"],
        "created_at": api_key_record["created_at"],
        "expires_at": api_key_record["expires_at"],
        "is_active": api_key_record["is_active"],
    }


# object = {
#         "id": "_id",
#         "name": name,
#         "api_key_hash": hashed_api_key,
#         "created_at": data.get("created_at"),
#         "expires_at": data.get("expires_at"),
#         "user_id": user_uuid,
#         "is_active": True,
#     }
