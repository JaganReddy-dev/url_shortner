from fastapi import APIRouter
from shortener_app.Services.user_service import user_details_service
from shortener_app.Schemas.create_users_request_schema import UserSchema

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "/add",
    summary="Add new user",
    description="Create a new user and generate an API key",
)
def create_user(user: UserSchema):
    return user_details_service(user.name)
