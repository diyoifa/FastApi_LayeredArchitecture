# from app.routes.user_routes import router
from app.services.user_service import find_user, create_user
from fastapi import status, Body
from app.models.user import UserIn


from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: str):
    return await find_user("_id", user_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserIn)
async def create_user_route(user: UserIn = Body(..., example={
    "username": "johndoe",
    "email": "JohnDoe@gmail.com",
    "password": "123"
})):
    return await create_user(user)