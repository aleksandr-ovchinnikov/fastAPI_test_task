import os
import shutil
from typing import List
import uuid
from datetime import datetime, date

from fastapi import APIRouter, Depends, File, UploadFile, status
from sqlalchemy.orm import Session
from .database import get_db
from db import db_image
from .schemas import ImageBase, UserBase
from auth.oauth2 import oauth2_scheme, get_current_user

router = APIRouter(
    tags=['image']
)


@router.delete('/frame/{code}')
def delete_images_by_code(code: str, db: Session = Depends(get_db)):
    names = db_image.get_image_name_by_code(db, code)
    for name in names:
        os.remove(f"./data/{name}")
    return db_image.delete_images_by_code(db, code)


@router.put('/frame')
def create_image(db: Session = Depends(get_db), upload_files: List[UploadFile] = File(...)):
    try:
        os.mkdir(f"./data")
    except:
        pass

    for upload_file in upload_files:
        myuuid = str(uuid.uuid4())
        path = f"data/{myuuid}.{upload_file.content_type.split('/')[-1]}"
        with open(path, "w+b") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
        day_time = date.today().strftime("%d.%m.%Y") + ' / ' + \
            datetime.now().strftime("%H:%M:%S")

        image = ImageBase
        image.code = status.HTTP_201_CREATED
        image.name = f"{myuuid}.{upload_file.content_type.split('/')[-1]}"
        image.date = day_time
        db_image.create_image_v2(db, image)

    return "done"


@router.get('/frame/{code}')  # , response_model=List[ImageBase])
def get_images_by_code(code: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        "data": db_image.get_images_by_code(db, code),
        "current_user": {
            current_user.username,
            current_user.email
        }
    }
