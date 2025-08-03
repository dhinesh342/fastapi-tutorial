from fastapi import Depends,HTTPException,status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
import jwt
from . import JWTtoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="authentication")

def get_current_user(token:str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return JWTtoken.verify_token(token,credentials_exception)
    # user = get_user(fake_users_db, username=token_data.username)
    # if user is None:
    #     raise credentials_exception
    # return user
