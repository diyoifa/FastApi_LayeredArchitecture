from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
from jose import jwt, JWTError
from ..config.dotenv import SECRET_KEY, ALGORITHM
from ..repositories.user_repository import find
from ..models.user import UserBase

async def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

oAuth2 = OAuth2PasswordBearer(tokenUrl='/login')

async def auth_user(token:str = Depends(oAuth2)):
    try:
        print("entre al auth_user")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        user =  await find("_id", user_id)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials", headers={"WWW-Authenticate": "Bearer"})
        return UserBase(id=str(user["_id"]), username=user["username"], email=user["email"]) 
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials", headers={"WWW-Authenticate": "Bearer"}) from exc
