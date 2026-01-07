from fastapi import APIRouter
from shortener_app.Services.user_services.create_user import new_user_service
from shortener_app.Models.v1.request.create_user import UserRequest
from shortener_app.Models.v1.response.create_user import UserResponse


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "/new",
    summary="Create a new user",
    description="Create a new user in the system when provided with a valid user name.",
    response_model=UserResponse,
    status_code=201,
)
async def create_user(user: UserRequest):
    """Create a new user."""
    return await new_user_service(user.name)

@router.get(
    "/{user_uuid}/urls",
    summary="Get urls associated with a user",
    description="Retrieves all URL mappings belonging to the user, returned as a list of objects containing long URLs and their corresponding short URLs.",
    response_model=UserResponse,
    status_code=200,
)