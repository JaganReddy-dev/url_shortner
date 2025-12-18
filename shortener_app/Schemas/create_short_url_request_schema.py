from pydantic import BaseModel


class CreateURLRequestSchema(BaseModel):
    url: str
    api_key: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "url": "https://www.google.com",
                    "api_key": "GLGDTYXEEAUUNRH8H6LN8TWOUJ9F",
                }
            ]
        },
        "extra": "forbid",
    }
