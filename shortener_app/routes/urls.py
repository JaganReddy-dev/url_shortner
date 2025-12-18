from fastapi import APIRouter
from shortener_app.Schemas.create_short_url_request_schema import CreateURLRequestSchema
from shortener_app.Services.url_service import (
    get_short_url_by_id_service,
    create_short_url_service,
    redirect_service,
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
def create_short_url(payload: CreateURLRequestSchema):
    return create_short_url_service(payload.url, payload.api_key)


@router.get(
    "/{url_id}",
    summary="Get the short URL for the user associated with the provided URL ID",
    description="Retrieve the short URL associated with the user identified by the provided URL ID.",
)
def get_short_url(url_id: str):
    return get_short_url_by_id_service(url_id)


@router.get(
    "/redirect/{url_id}",
    summary="Redirect to the long URL associated with the provided URL ID",
    description="Redirect to the long URL associated with the provided URL ID.",
)
def redirect_url(url_id: str):
    return redirect_service(url_id)
