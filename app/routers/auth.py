from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from ..schemas import CreateRegisteredUsers, RegistrationResponse
from ..database import get_db
from .. import models,util, oauth2

router = APIRouter(prefix = "/auth", tags=["AUTHENTICATION"])

#Signup endpoint
@router.post("/signup", status_code = status.HTTP_201_CREATED, response_model=RegistrationResponse)
async def register_user (user_details: CreateRegisteredUsers, db: Session = Depends (get_db)):

    hashed_password = util.hash(user_details.userPassword)
    user_details.userPassword = hashed_password
    
    user_name = db.query(models.RegisteredUsers).filter(models.RegisteredUsers.userName == user_details.userName).first()

    if  user_name is not None:
        raise HTTPException(status_code = status.HTTP_405_METHOD_NOT_ALLOWED, 
                            detail = "Username already exists") 
    
    new_user = models.RegisteredUsers(**user_details.model_dump())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

#Log in endpoint  
@router.post("/login", status_code = status.HTTP_200_OK)
async def login(user_details : OAuth2PasswordRequestForm = Depends(), db : Session = Depends (get_db)):

    user = db.query(models.RegisteredUsers).filter(models.RegisteredUsers.userName == user_details.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail = "Credentials entered are Incorrect")
    
    if not util.verify(user_details.password, user.userPassword):
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail = "Credentials entered are Incorrect")
    
    acess_token = oauth2.create_acess_tokens(data = {"sub": user.userName})

    return {"acess_token":acess_token, "token_type": "Bearer"}






