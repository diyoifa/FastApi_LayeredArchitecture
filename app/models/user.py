from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    id: str | None = None
    username: str | None = Field(None, min_length=3, description="Username of the user")
    email: EmailStr = Field(..., description="Email of the user")

class UserIn(UserBase):
    password: str = Field(..., min_length=3, description="Password of the user")



