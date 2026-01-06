from pydantic import BaseModel, Field
from datetime import datetime, timezone


class API_KEY_MODEL(BaseModel):
    id: str = Field(alias="_id")
    name: str
    api_key: str
    created_at: datetime = datetime.now(timezone.utc)
    expires_at: datetime = datetime.now(timezone.utc)
    user_id: str
    is_active: bool
