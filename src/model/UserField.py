from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..config.DbConfig import DbConfig

db_config = DbConfig()

class UserField(db_config.Base):
    __tablename__ = 'user_field'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    creation_date = Column(DateTime, nullable=False)