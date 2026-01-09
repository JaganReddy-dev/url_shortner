# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UserSignUpResponse(BaseModel):
    """Model for successful signup response"""

    user_uuid: str = Field(..., description="Unique user identifier")
    email: str = Field(..., description="User's email address")
    username: str = Field(..., description="User's username")
    created_at: datetime
    message: str = Field(
        default="User registered successfully", description="Success message"
    )


class UserInDB(BaseModel):
    """Model for user data stored in database"""

    email: str
    username: str
    hashed_password: str
    first_name: str
    last_name: str
    phone_number: Optional[str] = None
    is_active: bool = True
    is_verified: bool = False
    created_at: datetime
    updated_at: datetime
