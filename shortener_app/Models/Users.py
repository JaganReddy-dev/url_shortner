from pydantic import BaseModel
from datetime import datetime
from pydantic import Field


class UserModel(BaseModel):
    id: str = Field(alias="_id")
    user_name: str
    is_active: bool = True
    created_at: datetime
    updated_at: datetime

    class Config:
        populate_by_name = True
