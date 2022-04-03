from sqlalchemy import Column, String, Integer
from .database import Base


class Image(Base):
    __tablename__ = 'inbox'

    code = Column(String)
    name = Column(String, primary_key=True, unique=True, index=True)
    date = Column(String, index=True)


class DBUser(Base):
    __tablename__ = 'all_users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
