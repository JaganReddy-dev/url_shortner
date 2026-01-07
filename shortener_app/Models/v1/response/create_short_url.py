from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class URLResponse(BaseModel):
    id: str
    short_url_path: str
    status: Literal["created", "already_active", "reactivated"]
    long_url: str | None = None  # Only present for "created"
    created_at: datetime | None = None  # Only present for "created"
    expires_at: datetime | None = None  # Only present for "created"
    user_id: str | None = None  # Only present for "created"
    is_active: bool | None = None  # Only present for "created"
