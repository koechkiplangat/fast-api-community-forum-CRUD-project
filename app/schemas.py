from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CreateRegisteredUsers(BaseModel):
    username: EmailStr
    password : str
    #registered_at: Optional[datetime]

    #class Config:
        #orm_mode = True

class CreateSuperUser(BaseModel):
    username: EmailStr
    password : str

class RegistrationResponse(BaseModel):
    username: EmailStr
    registered_at: datetime


class TokenData(BaseModel):
    username: str | None = None


class UserPost(BaseModel):
     
     tittle: str
     category:Optional[str]="BATTERIES"
     body: str

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


