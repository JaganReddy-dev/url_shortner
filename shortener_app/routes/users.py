from fastapi import APIRouter
from pydantic import BaseModel
from shortener_app.service.user_service import user_details_service

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


class User(BaseModel):
    name: str


@router.post(
    "/add",
    summary="Add new user",
    description="Create a new user and generate an API key",
)
def create_user(user: User):
    return user_details_service(user.name)
