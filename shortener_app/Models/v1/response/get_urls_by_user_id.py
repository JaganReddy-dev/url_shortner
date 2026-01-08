from typing import List
from pydantic import BaseModel


class UrlItem(BaseModel):
    long_url: str
    short_url_path: str


class GetUrlsByUserIdResponse(BaseModel):
    res: List[UrlItem]
