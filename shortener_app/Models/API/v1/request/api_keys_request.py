from pydantic import BaseModel, Field


class APIKeyRequest(BaseModel):
    user_uuid: str = Field(
        alias="_id", description="UUID of the user who owns the API key"
    )
    api_key_name: str = Field(description="Name of the API key")
