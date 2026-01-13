from fastapi import APIRouter
from shortener_app.Models.V1.Response.get_urls_by_user_id import GetUrlsByUserIdResponse
from shortener_app.Services.user.get_urls_by_user_id import (
    get_urls_by_user_id_service,
)


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get(
    "/{user_uuid}/urls",
    summary="Get urls associated with a user",
    description="Retrieves all URL mappings belonging to the user, returned as a list of objects containing long URLs and their corresponding short URLs.",
    response_model=GetUrlsByUserIdResponse,
    status_code=200,
)
async def get_urls_by_user_id(user_uuid: str):
    """Get all URLs associated with a user by user ID."""
    return await get_urls_by_user_id_service(user_uuid)
