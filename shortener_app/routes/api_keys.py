from fastapi import APIRouter
from shortener_app.Services.api_key_service import create_api_key_service
from shortener_app.Models.API.v1.response.api_keys_response import APIKeyResponse
from shortener_app.Models.API.v1.request.api_keys_request import APIKeyRequest


router = APIRouter(
    prefix="/api_keys",
    tags=["api_keys"],
    responses={404: {"description": "user_uuid and name are required"}},
)


@router.post(
    "/",
    summary="Create an API Key",
    description="Generate a API Key when provided with a user uuid and a valid API key name.",
    response_model=APIKeyResponse,
)
def create_api_key(api_key_data: APIKeyRequest):
    """Create a new API key for the user."""
    result = create_api_key_service(api_key_data.user_uuid, api_key_data.api_key_name)
    return result
