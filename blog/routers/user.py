from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas,database,models
from ..services import user
from ..oauth2 import get_current_user

router=APIRouter(
    prefix="/user",
    tags=["users"]
)
get_db=database.get_db

@router.post("/",response_model=schemas.ShowUser,)
def create_user(request:schemas.User,db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return user.create(request,db)

@router.get("/{id}",response_model=schemas.ShowUser,)
def get_user(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return user.get(id,db)