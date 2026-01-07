from pydantic import BaseModel
from datetime import datetime


class UserResponse(BaseModel):
    id: str
    user_name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
