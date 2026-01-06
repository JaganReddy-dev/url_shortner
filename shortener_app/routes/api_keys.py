from fastapi import APIRouter
from shortener_app.Services.api_key_service import create_api_key_service

router = APIRouter(
    prefix="/api_keys",
    tags=["api_keys"],
    responses={404: {"description": "Cannot Insert if user_uuid or name is missing"}},
)


@router.post(
    "/",
    summary="Create an API Key",
    description="Generate a API Key when provided with a user uuid and a valid API key name.",
)
def create_api_key(user_uuid: str, name: str):
    """Create a new API key for the user."""
    return create_api_key_service(user_uuid, name)
