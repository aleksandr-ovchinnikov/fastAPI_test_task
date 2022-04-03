from typing import Optional
from pydantic import BaseModel


class ImageBase(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    date: Optional[str] = None

    class Config:
        orm_mode = True


# class UserBase(BaseModel):
#     username: str
#     email: str
#     password: str

#     class Config():
#         orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config():
        orm_mode = True
