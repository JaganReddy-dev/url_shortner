from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    model_config = {"json_schema_extra": {"examples": [{"name": "USER_NAME"}]}}
