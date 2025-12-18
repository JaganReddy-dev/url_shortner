from shortener_app.utilities.url_id_generator import url_id_generator
from shortener_app.data.url_details import url_store
from shortener_app.data.user_details import user_store
from shortener_app.utilities.find_key_by_value import (
    find_user_uuid_by_url_id,
    find_user_uuid_by_api_key,
)

base_url = "http://www.short.com/"


def create_short_url_service(url: str, api_key: str) -> dict:
    if not url or not api_key:
        return {"message": "URL and API key are required!"}
    user_id = find_user_uuid_by_api_key(user_store, api_key)
    if not user_id:
        return {"message": "Invalid API key!"}
    url_id = url_id_generator(url)
    url_data = {
        "url": url,
        "unique_id": url_id,
        "short_url": base_url + url_id,
    }
    url_store[user_id] = url_data
    return url_data


def get_short_url_service(url_id: str) -> dict:
    user_id = find_user_uuid_by_url_id(user_store, url_id)
    if not user_id:
        return {"message": "Invalid URL ID!"}
    return url_store[user_id]["short_url"]


# def url_get_service(api_key: str, url: str) -> dict:
#     return {"unique_id": unique_id, "api_key": api_key}
"""
- create data methods to add new url, update url, delete url
- update service to use the data methods
- update api to use service
- implement schema to validate request body 
- prepare resposne models for documentation
"""
# new_url = create_short_url_service(
#     "google.com",
#     "GLGDTYXEEAUUNRH8H6LN8TWOUJ9F",
# )

# print(new_url)

# {'url': 'google.com', 'unique_id': '05c4VCkJ', 'short_url': 'http://www.short.com/05c4VCkJ'}
