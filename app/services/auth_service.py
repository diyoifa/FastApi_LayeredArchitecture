from ..models.user import UserIn, UserCredentials
from ..utils.crypt import check_encrypted_password
from ..middlewares.authentication import create_access_token
from ..repositories.user_repository import find
from fastapi import HTTPException, status

async def validate_user_credentials(user: UserIn):
    user_db = await find("email", user.email)
    if user_db is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    
    if not check_encrypted_password(user.password, user_db["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

    token = await create_access_token(
        {
            "id": str(user_db["_id"]),
            "username": user_db["username"],
            "email": user.email
        }
    )

    return UserCredentials(id=str(user_db["_id"]), username=user_db["username"], email=user.email, token=token)