from fastapi import APIRouter
from shortener_app.Services.new_url_Service import create_new_short_url_service

router = APIRouter(
    prefix="/urls",
    tags=["urls"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    summary="Generate a short URL path for given long URL",
    description="Generates a short URL path if API key is valid and long URL is provided.",
)
def generate_short_url_path(long_url: str, api_key: str):
    return create_new_short_url_service(long_url, api_key)
