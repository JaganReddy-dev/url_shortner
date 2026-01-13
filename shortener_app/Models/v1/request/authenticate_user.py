# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY
from pydantic import BaseModel, Field, EmailStr


class AuthenticateUserRequest(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    password: str
