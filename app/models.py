from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import text
from sqlalchemy_utils.types import ChoiceType

from .database import Base

class UserPosts(Base):

    POSTS_TOPICS = (
        ('LIFEPO4','LiFePo4'),
        ('Solar','solar'),
        ('E-BIKES','e-bikes'),
        ('BATTERIES', 'batteries')

    )
     
    __tablename__ = "user_posts"

    id = Column(Integer, primary_key=True, nullable=False)
    tittle = Column (String (255), nullable = False)
    category = Column(ChoiceType(choices=POSTS_TOPICS),default="BATTERIES")
    body = Column (String, nullable = False)
    created_at = Column (TIMESTAMP(timezone=True), server_default= text ('now()'))
    author_id = Column (Integer, nullable = False)
    #superuser_post_id = Column  (Integer, ForeignKey ("superusers.id", ondelete = "CASCADE"), nullable = False)


class RegisteredUsers (Base):
    __tablename__ ="users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable = False, unique=True)
    password = Column(String, nullable = False)
    registered_at = Column (TIMESTAMP(timezone=True), server_default= text ('now()'))


class Replies (Base):
    __tablename__ = "replies"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column (String, nullable = False)
    comment_created_at = Column (TIMESTAMP(timezone=True), server_default= text ('now()'))
    author_id = Column (Integer, ForeignKey ("users.id", ondelete = "CASCADE"), nullable = False)
    superuser_post_id = Column  (Integer, ForeignKey ("superusers.id", ondelete = "CASCADE"), nullable = False)
    parent_post = Column (Integer, ForeignKey ("user_posts.id", ondelete = "CASCADE"), nullable = False)

    

