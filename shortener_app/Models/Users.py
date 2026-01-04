from pydantic import BaseModel
from datetime import datetime


class UserModel(BaseModel):
    user_id: str
    user_name: str
    is_active: bool = True
    created_at: datetime
    updated_at: datetime
