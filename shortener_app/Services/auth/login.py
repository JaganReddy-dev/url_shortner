from shortener_app.Utils.auth.hash_value import hash_password
from shortener_app.Models.V1.Request.authenticate_user import AuthenticateUserRequest
from shortener_app.Data.DB.mongo_client import user_collection as user


async def authenticate_user_service(user_details: AuthenticateUserRequest) -> bool:
    hashed_password = hash_password(user_details.password)

    result = await user.find_one(
        {
            "email": str(user_details.email),
            "password": hashed_password,
            "user_uuid": user_details.user_uuid,
        }
    )

    if hashed_password == result.get("password"):
        return True
    return False
