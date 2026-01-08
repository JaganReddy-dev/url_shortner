from shortener_app.Data.DB.mongo_client import url_map_collection
from shortener_app.Models.v1.response.get_urls_by_user_id import GetUrlsByUserIdResponse


async def get_urls_by_user_id_service(
    user_uuid: str,
) -> GetUrlsByUserIdResponse:
    """
    Retrieve all URL mappings associated with a given user ID.

    Args:
        user (GetUrlsByIdRequest): The user whose URL mappings are to be retrieved.

    Returns:
        list[dict]: A list of URL mapping documents associated with the user ID.
    """
    url_mappings = []
    cursor = url_map_collection.find(
        {"user_id": user_uuid}, {"long_url": 1, "short_url_path": 1, "_id": 0}
    )
    async for document in cursor:
        url_mappings.append(
            {
                "long_url": document["long_url"],
                "short_url_path": document["short_url_path"],
            }
        )
    return GetUrlsByUserIdResponse(res=url_mappings)
