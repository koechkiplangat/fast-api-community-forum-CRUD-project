from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CreateRegisteredUsers(BaseModel): 
    firstName: str
    lastName:str
    userName: str
    userEmail: EmailStr
    userPassword : str
    isAdmin:  Optional[bool]

    #registered_at: Optional[datetime]

    #class Config:
        #orm_mode = True

class CreateSuperUser(BaseModel):
    username: EmailStr
    password : str

class RegistrationResponse(BaseModel):
    userName: EmailStr
    registeredAt: datetime


class TokenData(BaseModel):
    username: str | None = None


class UserPost(BaseModel):
     
    postTittle: str
    postCategory:Optional[str]="BATTERIES"
    postText: str

    class Config:
        orm_mode  = True

class PostsResponse(BaseModel):

    tittle : str
    category : str
    created_at : str
    author_id : int


class UserReplies(BaseModel):

    content : str

class Announcements(BaseModel):
    title: str
    body: str

class FAQResources(BaseModel):
    title: EmailStr
    body: str



