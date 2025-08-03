from pydantic import BaseModel,Field,SecretStr
from typing import List


class Blog(BaseModel):
    title:str
    body:str



class User(BaseModel):
    name:str
    email:str
    password:SecretStr
    # password:str=Field(..., min_length=6, format="password")


class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]

class showBlog(BaseModel):
    title:str   
    body:str 
    creator:ShowUser
    # class Config():
    #     orm_mode=True

class Login(BaseModel):
    username:str
    password:str=Field(..., min_length=6, format="password")

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

