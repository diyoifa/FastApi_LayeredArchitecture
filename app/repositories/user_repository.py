from app.models.user import UserIn
from app.config.database import collection
from bson import ObjectId
from fastapi import HTTPException, status
from utils.crypt import encrypt_password

async def find(key, value):
    try:
        if key == "_id":
            user =  collection.find_one({key: ObjectId(value)})
        else:
            user =  collection.find_one({key: value})
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {key}={value} not found ")

async def create(user: UserIn):
    try: 
        user_dict = user.__dict__
        user_dict["password"] = encrypt_password(user.password)
        del user_dict["id"]
        print(user_dict)
        user_exist = await find("email", user.email)

        if user_exist:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

        id =  collection.insert_one(user_dict)
        new_user = await find("_id", id.inserted_id)
        return new_user

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {str(e)}")