from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    id: str | None = Field(None, description="ID of the user")
    username: str | None = Field(None, description="Username of the user")
    email: EmailStr = Field(..., description="Email of the user")

class UserIn(UserBase):
    password: str = Field(..., description="Password of the user")

class UserCredentials(UserBase):
    token: str = Field(..., description="Token of the user")
    token_type:str = "bearer"




