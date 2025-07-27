from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()


@app.get("/")
def root_route():
    return {"data":"root route to check server"}


@app.get("/blog")
def index(limit: int = 10, published:bool = False,sort:Optional[str]=None):
    # limit: int = 10, published:bool = False
    if published:
        return {"data":f"blog data limit is {limit} and is published."}
    else:
        return {"data": f"blog data limit is {limit} and is not published."}


@app.get("/blog/unpublished")
def unpublishedblog():
    return {"data":"All Unpublished blogs is here..."}


@app.get('/blog/{id}')
def show(id:int):
    return {"data":id}



@app.get("/blog/{id}/comments")
def comments(id : int,limit:int=10):
    return {"data":{"1","200",f"{limit}"}}

class Blog(BaseModel):
    title:str
    body:str
    publised:Optional[bool]=False

@app.post("/blog")
def create_blog(blog:Blog):
    # return blog
    return {"Data":{"Title":f"{blog.title}","Body":f"{blog.body}"}}



