from fastapi import APIRouter
from shortener_app.Models.V1.Request.authenticate_user import AuthenticateUserRequest
from shortener_app.Services.auth.login import authenticate_user_service

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login", response_model=bool, status_code=200)
async def create_user(user_data: AuthenticateUserRequest):
    """Authenticate a user and return a login response."""
    return await authenticate_user_service(user_data)
