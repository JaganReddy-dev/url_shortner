from shortener_app.Data.DB.mongo_client import user_collection
from shortener_app.Models.V1.Request.signup import UserSignUpRequest
from shortener_app.Models.V1.Response.signup import UserSignUpResponse
from shortener_app.Models.V1.Response.signup import UserInDB
from shortener_app.Utils.auth.hash_value import hash_password
from datetime import datetime, timezone


async def create_user_service(user_data: UserSignUpRequest):
    """Create a new user in the database."""
    hashed_password = hash_password(user_data.password)
    created_at = datetime.now(timezone.utc)
    document = UserInDB(
        email=str(user_data.email),
        username=user_data.username,
        hashed_password=hashed_password,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        phone_number=user_data.phone_number,
        is_active=True,
        is_verified=False,
        created_at=created_at,
        updated_at=created_at,
    )
    result = await user_collection.insert_one(document)

    return UserSignUpResponse(
        user_uuid=str(result.inserted_id),
        email=user_data.email,
        username=user_data.username,
        created_at=created_at,
    )
