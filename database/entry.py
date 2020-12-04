from sqlalchemy import Column, Integer, String
from .base import Base


class Entry(Base):
    __tablename__ = "entry"
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    image = Column(String)  # link to image
    link = Column(String)   # link to resource
    rank = Column(Integer, default=0)

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title
