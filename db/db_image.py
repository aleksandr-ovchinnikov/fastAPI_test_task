from sqlalchemy.orm import Session
from db.models import Image
from datetime import datetime, date
from .schemas import ImageBase

day_time = date.today().strftime("%d.%m.%Y") + ' / ' + \
    datetime.now().strftime("%H:%M:%S")


def create_image_v2(db: Session, request: ImageBase):
    new_image = Image(
        code=request.code,
        name=request.name,
        date=request.date
    )
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    return new_image


# def create_image(db: Session, request: dict):
#     new_image = Image(
#         code=request['code'],
#         name=request['name'],
#         date=day_time
#     )

#     db.add(new_image)
#     db.commit()
#     db.refresh(new_image)
#     return new_image


def get_images_by_code(db: Session, code: str):
    return db.query(Image).filter(Image.code == code).all()

# def get_images_by_code_v2(db: Session, code: str):


def delete_images_by_code(db: Session, code: str):
    images_to_delete = db.query(Image).filter(Image.code == code).all()
    for image_to_delete in images_to_delete:
        db.delete(image_to_delete)
        db.commit()


def get_image_name_by_code(db: Session, code: str):
    images_to_get = db.query(Image).filter(Image.code == code).all()
    return [x.name for x in images_to_get]
