from app.repositories.user_repository import find, create
from app.models.user import UserBase, UserIn

async def find_user(key:str, value):
    user = await find(key, value)
    return UserBase(id=str(user["_id"]), username=user["username"], email=user["email"])

async def create_user(user: UserIn):
    new_user = await create(user)
    print(new_user)
    return UserBase(id=str(new_user["_id"]), username=new_user["username"], email=new_user["email"])