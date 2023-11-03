from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
import asyncio

from datetime import datetime,timedelta
from jose import jwt, JWTError

from .schemas import TokenData
from .database import get_db
from . import models
from .config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

#Creating acess tokens

def create_acess_tokens (data:dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    acess_tokens = jwt.encode(to_encode, SECRET_KEY, algorithm  = ALGORITHM)

    return acess_tokens

credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})

exception_dependency: Annotated [str, Depends (credentials_exception)]

async def verify_acess_token (token: Annotated [str, Depends (oauth2_scheme)], exception_dependency):
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise exception_dependency
        token_data = TokenData(username=username)
    except JWTError:
        raise exception_dependency
    
    return token_data

async def get_current_user (token : str  = Depends(oauth2_scheme), db : Session =  Depends (get_db)):

    tokens =  await verify_acess_token(token, exception_dependency)

    user = db.query(models.RegisteredUsers).filter(models.RegisteredUsers.username == tokens.username).first()

    return user
