from shortener_app.Models.V1.Request.signup import UserSignUpRequest
from shortener_app.Models.V1.Response.signup import UserSignUpResponse
from shortener_app.Services.auth.signup import create_user_service
from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/signup", response_model=UserSignUpResponse)
async def create_user(user_data: UserSignUpRequest):
    """Create a new user in the database."""
    return await create_user_service(user_data)
