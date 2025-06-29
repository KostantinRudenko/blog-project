from datetime import datetime
from sqlalchemy import (Table, Column, Integer, String,
                        DateTime, Boolean, ForeignKey, create_engine)
from sqlalchemy.orm import backref, relationship, declarative_base

Base = declarative_base()

class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer(), primary_key=True)
    title = Column(String(128))
    content = Column(String())
    date = Column(DateTime(), default=datetime.now())

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer(), primary_key=True)
    post_id = Column(Integer(), ForeignKey('posts.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))
    content = Column(String())

    post = relationship("posts", backref=backref('comments', order_by=id))
    user = relationship("users", uselist=False)

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(28), unique=True, nullable=False)
    password = Column(String(), nullable=False)
    is_superuser = Column(Boolean(), default=False)

USERNAME = ...
PASSWORD = ...
HOST = "localhost"
PORT = 5432
DBNAME = "postgres"
URL = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
engine = create_engine(URL)
Base.metadata.create_all(bind=engine)
