from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from .base import Base


def get_session():
    engine = create_engine('sqlite:///feed.db', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = get_session()()
    try:
        yield session
        session.commit()
    except BaseException:
        session.rollback()
        raise
    finally:
        session.close()
