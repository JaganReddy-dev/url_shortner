from pydantic import BaseModel, HttpUrl, StringConstraints
from typing import Annotated


class URLRequest(BaseModel):
    long_url: HttpUrl
    api_key: Annotated[str, StringConstraints(min_length=28, max_length=28)]
