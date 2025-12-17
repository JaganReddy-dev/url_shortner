from shortener_app.utilities.url_id_generator import url_id_generator
from shortener_app.utilities.api_key_generator import api_key_generator
from shortener_app.data.url_details import url_store
import uuid

base_url = "http://www.short.com/"


def user_details_service(name: str) -> dict:
    api_key = api_key_generator()
    user_uuid = uuid.uuid4()
    api_key_name = name
    user_data = {"api_key": api_key, "api_key_name": api_key_name, "user id": user_uuid}
    url_store[user_uuid] = user_data
    return {k: v for k, v in user_data.items() if k != "user_id"}


def url_generator_service(url: str, api_key: str) -> dict:
    if url and api_key:
        url_id = url_id_generator(url)
        api_key = api_key_generator()
        url_data = {
            "unique_id": url_id,
            "url": url,
            "short_url": base_url + url_id,
            "api_key": api_key,
        }

    return url_data


def url_update_service(url: str, unique_id: str, api_key: str, new_url: str) -> dict:
    return {"unique_id": unique_id, "url": url}


def url_delete_service(unique_id: str, api_key: str) -> dict:
    return {"unique_id": unique_id, "message": "URL deleted successfully!"}


# def url_get_service(api_key: str, url: str) -> dict:
#     return {"unique_id": unique_id, "api_key": api_key}
"""
- create data methods to add new url, update url, delete url
- update service to use the data methods
- update api to use service
- implement schema to validate request body 
- prepare resposne models for documentation
"""
