from fastapi import APIRouter, Depends, HTTPException,  status
from sqlalchemy.orm import Session


from .. import models
from ..database import get_db
from ..oauth2 import  get_current_user
from .. schemas import UserPost, PostsResponse

router = APIRouter(prefix = "/posts", tags= ["POSTS"] )

#Creating new posts - meant for users who are creating a post
@router.post("/new_posts", status_code=status.HTTP_201_CREATED)
async def create_new_post(new_post: UserPost, db:  Session = Depends (get_db), current_user: str = Depends (get_current_user)):

    new_post = models.UserPosts(author_id = current_user.id,  **new_post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

#Getting all posts - For listing in the main window 

@router.get("/all_posts", status_code = status.HTTP_200_OK)
async def get_all_posts (db : Session  = Depends(get_db), current_user : str = Depends(get_current_user)):

    posts = db.query(models.UserPosts).all()

    return posts

#Getting specific posts 

@router.get("/posts/{id}", status_code=status.HTTP_200_OK)
async def get_specific_post (id  : int , db : Session  = Depends (get_db), current_user: str = Depends(get_current_user)):

    posts = db.query(models.UserPosts).filter(models.UserPosts.id == id).first()

    if posts is None:
        return HTTPException (status_code = status.HTTP_404_NOT_FOUND, 
                              detail  = f"Post of id no {id} is not available")
    return posts

#Getting My posts

@router.get("/my_posts", status_code=status.HTTP_200_OK)
async def get_my_posts (db : Session = Depends (get_db), 
                        current_user: str = Depends(get_current_user)):

    my_posts = db.query(models.UserPosts).filter(models.UserPosts.author_id == current_user.id).all()

    if my_posts:
        return my_posts
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = "User has no posts yet")

