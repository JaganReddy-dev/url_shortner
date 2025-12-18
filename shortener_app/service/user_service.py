from shortener_app.utilities.api_key_generator import api_key_generator
from shortener_app.data.user_details import user_store
import uuid

base_url = "http://www.short.com/"


def user_details_service(name: str) -> dict:
    api_key = api_key_generator()
    user_uuid = uuid.uuid4()
    api_key_name = name
    valid = True
    expires = 90
    user_data = {
        "api_key": api_key,
        "api_key_name": api_key_name,
        "valid": valid,
        "expires": expires,
        "user_uuid": user_uuid,
    }
    user_store[user_uuid] = user_data

    return user_data


# test_user = user_details_service("test")

# print(test_user)
# # {'api_key': 'nCC34wEp7li33g', 'api_key_name': 'test', 'valid': True, 'expires': 90}
