from fastapi import FastAPI


from .database import engine
from .models import Base

from .routers import auth, posts

Base.metadata.create_all(engine)

app = FastAPI()


app.include_router(auth.router)
app.include_router(posts.router)

