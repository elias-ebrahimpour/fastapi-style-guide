from datetime import datetime

from sqlalchemy import Column, Integer, String

from .database import Base


def created_at():
    return datetime.now()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(String, name="created_at", default=created_at)

    def dict(self):
        return self.__dict__
