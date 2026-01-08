from fastapi import APIRouter
from shortener_app.Services.url_services.create_short_url import (
    create_short_url_service,
)
from shortener_app.Models.v1.request.create_short_url import URLRequest
from shortener_app.Models.v1.response.create_short_url import URLResponse

router = APIRouter(
    prefix="/short_url",
    tags=["short_url"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/new",
    summary="Generate a short URL path for given long URL",
    description="Generates a short URL path if API key is valid and long URL is provided.",
    response_model=URLResponse,
)
async def generate_short_url_path(url_data: URLRequest):
    return await create_short_url_service(url_data.long_url, url_data.api_key)
