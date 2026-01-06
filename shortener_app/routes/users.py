from fastapi import APIRouter
from shortener_app.Services.new_user_service import new_user_service
from shortener_app.Schemas.ReqResSchemas.ReqSchemas.create_users_request_schema import (
    UserSchema,
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "/",
    summary="Add new user",
    description="Create a new user in the system.",
)
def create_user(user: UserSchema):
    return new_user_service(user.name)
