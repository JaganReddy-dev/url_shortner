from fastapi import APIRouter
from shortener_app.Services.new_user_service import new_user_service
from shortener_app.Models.v1.request.create_user_request import UserRequest
from shortener_app.Models.v1.response.create_user_response import UserResponse

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "/",
    summary="Create a new user",
    description="Create a new user in the system when provided with a valid user name.",
    response_model=UserResponse,
    status_code=201,
)
async def create_user(user: UserRequest):
    """Create a new user."""
    return await new_user_service(user.name)
