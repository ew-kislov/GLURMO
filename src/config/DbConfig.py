import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# NOTE: singleton class containing db variables


class DbConfig:
    Base = declarative_base()
    engine = create_engine(os.getenv("DB_PATH"))
    sesson_factory = sessionmaker(bind=engine)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DbConfig, cls).__new__(cls)
        return cls.instance