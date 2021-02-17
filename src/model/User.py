from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from ..model.UserFieldValue import UserFieldValue

from ..config.DbConfig import DbConfig

db_config = DbConfig()

class User(db_config.Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    uid = Column(Integer, nullable=False)
    is_admin = Column(Boolean, nullable=False)
    user_group_id = Column(Integer, ForeignKey('user_group.id'))
    creation_date = Column(DateTime, nullable=False)

    values = relationship('UserFieldValue')
    group = relationship('UserGroup')