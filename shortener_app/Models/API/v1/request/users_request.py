from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    model_config = {"json_schema_extra": {"examples": [{"name": "USER NAME"}]}}
