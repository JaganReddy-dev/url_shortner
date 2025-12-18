from fastapi import APIRouter
from shortener_app.service.url_service import (
    get_short_url_service,
    create_short_url_service,
)

router = APIRouter(
    prefix="/urls",
    tags=["urls"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/create",
    summary="Create a short URL for the provided long URL",
    description="Generate a short URL when provided with a long URL and a valid API key.",
)
def create_short_url(url: str, api_key: str):
    return create_short_url_service(url, api_key)


@router.get(
    "/{url_id}",
    summary="Get the short URL for the user associated with the provided URL ID",
    description="Retrieve the short URL associated with the user identified by the provided URL ID.",
)
def get_short_url(url_id: str):
    return get_short_url_service(url_id)
