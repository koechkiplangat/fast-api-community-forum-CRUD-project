from fastapi import APIRouter, Depends, HTTPException,  status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


from ..schemas import CreateSuperUser
from ..database import get_db
from ..util import verify, hash
from .. import admin_models, oauth2


router = APIRouter (prefix = "/admin/auth", tags =["ADMIN SIGNUP"])

# Superusers sign up

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def sign_up_admin(admin_details: CreateSuperUser, db: Session = Depends (get_db)):

    hashed_password = hash(admin_details.password)
    admin_details.password = hashed_password

    admin = db.query(admin_models.SuperUsers).filter(admin_models.SuperUsers.username == admin_details.usermane)

    if admin is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, 
                            detail = "Admin with similar credentials already exists")
    
    new_admin = admin_models.SuperUsers(**admin_details.model_dump())
    db.add(new_admin)
    db.comitt()
    db.refresh(new_admin)
    

#Superuser log in
@router.post("/login",  status_code = status.HTTP_200_OK)
async def log_in_admin(login_detail : OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    admin = db.query(admin_models.SuperUsers).filter(admin_models.SuperUsers.username == login_detail.username)

    if not admin:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                            detail= "Invalid credentials entered")
    
    if not verify(login_detail.password, admin.password):
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                            detail= "Invalid credentials entered")
    
    admin_acess_token = oauth2.create_acess_tokens(data = {"sub": admin.username})

    return {"acess_tokens": admin_acess_token , "token_type": "Bearer"}
        

        

        

