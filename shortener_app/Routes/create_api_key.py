from fastapi import APIRouter
from shortener_app.Services.api_key_service import create_api_key_service
from shortener_app.Models.v1.response.create_api_key_response import APIKeyResponse
from shortener_app.Models.v1.request.create_api_key_request import APIKeyRequest


router = APIRouter(
    prefix="/api_key",
    tags=["api_key"],
    responses={404: {"description": "user_uuid and name are required"}},
)


@router.post(
    "/",
    summary="Create an API Key",
    description="Generate a API Key when provided with a valid user uuid and a valid API key name.",
    response_model=APIKeyResponse,
    status_code=201,
)
async def create_api_key(api_key_data: APIKeyRequest):
    """Create a new API key for the user."""
    return await create_api_key_service(
        api_key_data.user_uuid, api_key_data.api_key_name
    )
