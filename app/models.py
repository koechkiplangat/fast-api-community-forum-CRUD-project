from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import text
from sqlalchemy_utils.types import ChoiceType
from typing import Optional

from .database import Base

class RegisteredUsers (Base):
    __tablename__ ="userDetail"

    userId = Column(Integer, primary_key=True, nullable=False)
    firstName = Column (String, nullable =False, unique =False)
    lastName = Column (String, nullable = False, unique = False)
    userName = Column(String, nullable = False, unique=True)
    userEmail = Column (String, unique =  True, nullable=False)
    userPassword = Column(String, nullable = False)
    isAdmin = Column (Optional[bool], default=False )
    registeredAt = Column (TIMESTAMP(timezone=True), server_default= text ('now()'))
 

class UserPosts(Base):

    POSTS_TOPICS = (
        ('LIFEPO4','LiFePo4'),
        ('Solar','solar'),
        ('E-BIKES','e-bikes'),
        ('BATTERIES', 'batteries')

    )
     
    __tablename__ = "userPost"

    postId = Column(Integer, primary_key=True, nullable=False)
    userId = Column (Integer, ForeignKey("userDetail.userId", ondelete= "CASCADE"), nullable = False)
    postCategory = Column(ChoiceType(choices=POSTS_TOPICS),default="BATTERIES")
    postTittle = Column (String (255), nullable = False)
    postText  = Column (String, nullable = False)
    createdAt = Column (TIMESTAMP(timezone=True), server_default= text ('now()'))
    

class Replies (Base):
    __tablename__ = "userComment"

    commentId = Column(Integer, primary_key=True, nullable=False)
    postId = Column (Integer, ForeignKey("userPost.postID", ondelete = "CASCADE"), nullable = False)
    userId = Column (Integer, ForeignKey("userDetail.userId", ondelete= "CASCADE"), nullable = False)
    contentText = Column (String, nullable = False)
    createdAt = Column (TIMESTAMP(timezone=True), server_default= text ('now()'))



