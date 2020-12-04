from sqlalchemy import Column, Integer, String
from .base import Base


class Entries(Base):
    __tablename__ = "entries"
    id = Column(Integer, autoincrement=True, primary_key=True)
    entry = Column(String)
