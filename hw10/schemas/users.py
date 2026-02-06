from pydantic import BaseModel
from typing import Optional

class UserLoginSchema(BaseModel):
    user_name:str
    password:str


class UserSchema(BaseModel):
    id: int
    username: Optional[str] = None

class UserResponseSchema(BaseModel):
    id: int
    username: Optional[str] = None
