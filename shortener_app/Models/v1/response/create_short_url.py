from datetime import datetime
from pydantic import BaseModel


class URLResponse(BaseModel):
    id: str
    short_url_path: str
    long_url: str
    created_at: datetime
    expires_at: datetime
    user_id: str
    is_active: bool
