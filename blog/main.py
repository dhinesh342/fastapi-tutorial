from fastapi import FastAPI,Depends,status,Response,HTTPException
# from typing import List
# from sqlalchemy.orm import Session
from . import models
from .database import engine,get_db
# from .hashing import Hash
from .routers import blog,user,authentication

app=FastAPI()

models.Base.metadata.create_all(engine)

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


