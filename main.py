from fastapi import FastAPI

from db import models
from db.database import engine
from db import image_crud
from auth import authentication
from router import user

app = FastAPI()
app.include_router(image_crud.router)
app.include_router(authentication.router)
app.include_router(user.router)


@app.get('/')
async def main():
    return{"msg": "hi there"}


models.Base.metadata.create_all(engine)
