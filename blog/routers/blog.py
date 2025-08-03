from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas,database,models
from ..services import blog
from ..oauth2 import get_current_user

router=APIRouter(
    prefix="/blog",
    tags=["blogs"]
)
get_db=database.get_db

@router.get("/",response_model=List[schemas.showBlog])
def get_all_blog(db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.get_all(db) 

@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db: Session=Depends(get_db)):
    return blog.create(request,db)

@router.get("/{id}",status_code=200,response_model=schemas.showBlog)
def get_blog(id:int,db:Session=Depends(get_db)):
    return blog.getby_id(id,db)


@router.delete("/{id}",status_code=status.HTTP_200_OK)
def delete_blog(id,db:Session=Depends(get_db)):
    return blog.delete(id,db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int,request:schemas.Blog,db:Session=Depends(get_db)):
    return blog.update(id,request,db)