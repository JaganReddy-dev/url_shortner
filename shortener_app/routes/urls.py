from fastapi import APIRouter
from shortener_app.Services.new_url_Service import create_new_short_url_service
from shortener_app.Models.API.v1.request.urls_request import URLRequest
from shortener_app.Models.API.v1.response.urls_response import URLResponse

router = APIRouter(
    prefix="/urls",
    tags=["urls"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    summary="Generate a short URL path for given long URL",
    description="Generates a short URL path if API key is valid and long URL is provided.",
    response_model=URLResponse,
)
def generate_short_url_path(url_data: URLRequest):
    return create_new_short_url_service(url_data.long_url, url_data.api_key)
