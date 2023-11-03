from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import text

from  . database import Base

class SuperUsers(Base):
    __tablename__ ="superusers"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable = False, unique=True)
    password = Column(String, nullable = False)
    ceeated_at = Column (TIMESTAMP(timezone=True), server_default= text ('now()'))

class Announcements (Base):
    __tablename__  = "broadcast"

    id = Column(Integer, primary_key=True, nullable=False)
    tittle = Column (String (15), nullable = False)
    body = Column (String, nullable = False)
    created_at = Column (TIMESTAMP(timezone=True), server_default= text ('now()'))
    author_id = Column (Integer, ForeignKey ("superusers.id"), nullable = False)

class FAQResources(Base):
    __tablename__ = "faq"

    id = Column(Integer, primary_key=True, nullable=False)
    tittle = Column (String (15), nullable = False)
    body = Column (String, nullable = False)
    author_id = Column (Integer, ForeignKey ("superusers.id"), nullable = False)





    



