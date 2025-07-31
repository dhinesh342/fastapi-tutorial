from pydantic import BaseModel
from typing import List


class Blog(BaseModel):
    title:str
    body:str



class User(BaseModel):
    name:str
    email:str
    password:str

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

