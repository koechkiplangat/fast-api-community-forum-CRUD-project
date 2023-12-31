from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import text
from sqlalchemy_utils.types import ChoiceType


from .database import Base

class RegisteredUsers (Base):
    __tablename__ ="userDetail"

    userId = Column(Integer, primary_key=True, nullable=False, unique = True)
    firstName = Column (String, nullable =False, unique =False)
    lastName = Column (String, nullable = False, unique = False)
    userName = Column(String, nullable = False, unique=True)
    userEmail = Column (String, unique =  True, nullable=False)
    userPassword = Column(String, nullable = False)
    isAdmin = Column(Boolean, default=False )
    registeredAt = Column (TIMESTAMP(timezone=True), server_default= text ('now()'))
 

class UserPosts(Base):

    POSTS_CATEGORY = (
        ('LIFEPO4','LiFePo4'),
        ('Solar','solar'),
        ('E-BIKES','e-bikes'),
        ('BATTERIES', 'batteries'),
        ('SHARE_PROJECTS','share_projects')


    )
     
    __tablename__ = "userPost"

    postId = Column(Integer, primary_key=True, nullable=False)
    userId = Column (Integer, ForeignKey("userDetail.userId", ondelete= "CASCADE"), nullable = False)
    postCategory = Column(ChoiceType(choices=POSTS_CATEGORY),default="BATTERIES")
    postTittle = Column (String (255), nullable = False)
    postText  = Column (String, nullable = False)
    createdAt = Column (TIMESTAMP(timezone=True), server_default= text ('now()'), nullable = False)
    

class Replies (Base):
    __tablename__ = "userComment"

    commentId = Column(Integer, primary_key=True, nullable=False)
    postId = Column (Integer, ForeignKey("userPost.postId", ondelete = "CASCADE"), nullable = False)
    userId = Column (Integer, ForeignKey("userDetail.userId", ondelete= "CASCADE"), nullable = False)
    contentText = Column (String, nullable = False)
    createdAt = Column (TIMESTAMP(timezone=True), server_default= text ('now()'))



