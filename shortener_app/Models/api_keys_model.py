from pydantic import BaseModel, Field
from datetime import datetime, timezone


class API_KEY_MODEL(BaseModel):
    id: str = Field(alias="_id")
    name: str
    api_key_hash: str
    created_at: int = int(datetime.now(timezone.utc).timestamp())
    expires_at: int = int(datetime.now(timezone.utc).timestamp()) + (30 * 24 * 60 * 60)
    user_id: str
    is_active: bool


# object = {
#         "id": "_id",
#         "name": name,
#         "api_key_hash": hashed_api_key,
#         "created_at": data.get("created_at"),
#         "expires_at": data.get("expires_at"),
#         "user_id": user_uuid,
#         "is_active": True,
#     }
