from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict
from typing import Optional
import re


class UserSignUpRequest(BaseModel):
    """Model for user signup request validation"""

    model_config = ConfigDict(str_strip_whitespace=True)

    email: EmailStr = Field(
        ..., description="User's email address", examples=["user@example.com"]
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="User password (8-128 characters)",
        examples=["SecurePass123!"],
    )

    username: str = Field(
        ...,
        min_length=8,
        max_length=30,
        description="Unique username (8-30 characters, alphanumeric and underscore only)",
        examples=["john_doe"],
    )

    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="User's first name",
        examples=["John"],
    )

    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="User's last name",
        examples=["Doe"],
    )

    phone_number: Optional[str] = Field(
        None, description="Optional phone number", examples=["+1234567890"]
    )

    terms_accepted: bool = Field(
        ..., description="User must accept terms and conditions", examples=[True]
    )

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        """Validate password meets security requirements"""
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")

        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")

        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError("Password must contain at least one special character")

        return v

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        """Validate username format"""
        if not re.match(r"^[a-zA-Z0-9_]+$", v):
            raise ValueError(
                "Username can only contain letters, numbers, and underscores"
            )

        if v[0].isdigit():
            raise ValueError("Username cannot start with a number")

        return v.lower()

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, v: Optional[str]) -> Optional[str]:
        """Validate phone number format"""
        if v is None:
            return v

        # Remove common separators
        cleaned = re.sub(r"[\s\-\(\)]", "", v)

        # Check if it's a valid phone number (basic validation)
        if not re.match(r"^\+?\d{10,15}$", cleaned):
            raise ValueError(
                "Invalid phone number format. Use international format (+1234567890)"
            )

        return cleaned

    @field_validator("terms_accepted")
    @classmethod
    def validate_terms(cls, v: bool) -> bool:
        """Ensure terms are accepted"""
        if not v:
            raise ValueError("You must accept the terms and conditions")
        return v
