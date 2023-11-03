from fastapi import FastAPI


from .database import engine
from .models import Base

from .routers import auth, admin_auth, posts

Base.metadata.create_all(engine)

app = FastAPI()


app.include_router(auth.router)
app.include_router(admin_auth.router)
app.include_router(posts.router)