from ..services.user_service import find_user, find_all_users, create_user, update_user, delete_user, delete_all_users
from fastapi import  status, Body, Request, Depends
from ..models.user import UserIn, UserBase
from ..middlewares.authentication import auth_user


from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users():
    return await find_all_users()

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: str):
    return await find_user("_id", user_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserBase)
async def create_user_route(user: UserIn = Body(..., example={
    "username": "johndoe",
    "email": "JohnDoe@gmail.com",
    "password": "123"
})):
    return await create_user(user)

@router.patch("/", status_code=status.HTTP_200_OK, response_model=UserBase)
async def update_user_route(request: Request, user = Depends(auth_user)):
    return await update_user(request, user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_route(user_id: str):
    await delete_user(user_id)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_users_route():
    await delete_all_users()
