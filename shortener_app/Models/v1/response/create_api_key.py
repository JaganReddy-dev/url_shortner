from pydantic import BaseModel, Field
from datetime import datetime


class APIKeyResponse(BaseModel):
    id: str
    name: str
    api_key: str = Field(..., min_length=28, max_length=28)
    created_at: datetime
    expires_at: datetime
    user_id: str
    is_active: bool
