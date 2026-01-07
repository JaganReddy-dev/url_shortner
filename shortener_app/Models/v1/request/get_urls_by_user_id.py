from pydantic import BaseModel


class GetUrlsByIdRequest(BaseModel):
    user_uuid: str
