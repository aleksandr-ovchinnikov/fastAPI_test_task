from importlib.metadata import files
from typing import List
from fastapi import Depends, Path, UploadFile, status
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from main import app
from db.database import Base, get_db
from datetime import datetime, date

day_time = date.today().strftime("%d.%m.%Y") + ' / ' + \
    datetime.now().strftime("%H:%M:%S")

SQLACHEMY_DATABASE_URL = "postgresql://theblindone:password@localhost/test_db"

engine = create_engine(SQLACHEMY_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hi there"}


def test_create_image():
    _test_image = "data/21a727b4-74f6-4dfb-b95b-a81b3367a488.png"
    _files = {'upload_files': _test_image}
    response = client.put(
        "/frame",
        files=_files
    )
    assert response.status_code == status.HTTP_200_OK


# def test_image():
#     response = client.put(
#         "/frame",
#         files={'upload_file': test_image.open('rb')}
#     )
#     # with TestClient(app) as client:
#     response = client.post('/frame',
#                            files=test_image)
#     assert response.status_code == status.HTTP_200_OK
