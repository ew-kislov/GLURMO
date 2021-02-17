from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .UserField import UserField

from ..config.DbConfig import DbConfig

db_config = DbConfig()


class LimitItem(db_config.Base):
    __tablename__ = 'limit_item'

    id = Column(Integer, primary_key=True)
    user_field_id = Column(Integer, ForeignKey('user_field.id'))
    max_value = Column(Integer, nullable=False)

    user_field = relationship('UserField')