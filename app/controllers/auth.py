from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from ..models.user import UserIn, UserCredentials
from ..services.auth_service import validate_user_credentials

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/", status_code=status.HTTP_302_FOUND, response_model=UserCredentials)
async def auth_user(user: UserIn):
    user_credentials = await validate_user_credentials(user)
    return user_credentials



