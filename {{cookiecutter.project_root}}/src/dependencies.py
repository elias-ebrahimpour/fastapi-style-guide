
from .database import SessionLocal


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def db_instance():
    return next(get_db())
