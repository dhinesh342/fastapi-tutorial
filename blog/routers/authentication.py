from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from .. import schemas,database,models
from ..hashing import Hash
from ..JWTtoken import create_access_token



router=APIRouter(
    tags=["authentication"]
)

get_db=database.get_db

ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/login")
def login(request:schemas.Login,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email== request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"username not found {request.username}")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"user {request.username} wrong password")
    
    #generate JWT and return
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token":access_token, "token_type":"bearer"}