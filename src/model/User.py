from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from model.UserFieldValue import UserFieldValue

from config.DbConfig import DbConfig

db_config = DbConfig()

class User(db_config.Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    is_admin = Column(Boolean, nullable=False)
    creation_date = Column(DateTime, nullable=False)

    values = relationship('UserFieldValue')