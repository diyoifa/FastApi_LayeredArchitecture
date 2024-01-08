from fastapi import Request, HTTPException, status, Depends
from ..repositories.user_repository import find, find_all, create, update, delete, delete_all
from ..models.user import UserBase, UserIn
from ..utils.crypt import encrypt_password


async def find_all_users():
    users = await find_all()
    return [UserBase(id=str(user["_id"]), username=user["username"], email=user["email"]) for user in users]

async def find_user(key:str, value):
    user = await find(key, value)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserBase(id=str(user["_id"]), username=user["username"], email=user["email"])

async def create_user(user: UserIn):
    new_user = await create(user)
    # print(new_user)
    return UserBase(id=str(new_user["_id"]), username=new_user["username"], email=new_user["email"])

async def update_user(request: Request, user_id:str):
    body = await request.json()
    # user_id = user.id
    if "password" in body:
        body["password"] = encrypt_password(body["password"])
        updated_user = await update(user_id, body)
    else:
        updated_user = await update(user_id, body)
    return UserBase(id=str(updated_user["_id"]), username=updated_user["username"], email=updated_user["email"])
    

async def delete_user(user_id: str):
    await delete(user_id)
    
async def delete_all_users():
    await delete_all()