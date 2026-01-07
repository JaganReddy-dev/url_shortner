from fastapi import APIRouter
from shortener_app.Services.new_user_service import new_user_service
from shortener_app.Models.API.v1.request.users_request import UserRequest

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "/",
    summary="Add new user",
    description="Create a new user in the system.",
    response_model=None,
)
def create_user(user: UserRequest):
    result = new_user_service(user.name)
    return result
