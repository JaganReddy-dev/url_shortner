from shortener_app.Utils.auth.hash_value import hash_password
from shortener_app.Models.V1.Request.authenticate_user import AuthenticateUserRequest
from shortener_app.Data.DB.mongo_client import user
from shortener_app.Utils.auth.jwt import generate_jwt_token
from datetime import datetime, timedelta, timezone


async def authenticate_user_service(user_details: AuthenticateUserRequest):
    hashed_password = hash_password(user_details.password)

    result = await user.find_one(
        {
            "email": str(user_details.email),
            "password": hashed_password,
            "user_uuid": user_details.user_uuid,
        }
    )

    if hashed_password == result.get("password"):
        payload = {
            "user_uuid": user_details.user_uuid,
            "exp": datetime(timezone.utc) + timedelta(minutes=15),
            "iat": datetime(timezone.utc),
            "email": user_details.email,
            "roles": result.get("roles"),
        }
