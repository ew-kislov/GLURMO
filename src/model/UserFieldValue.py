from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from model.UserField import UserField

from config.DbConfig import DbConfig

db_config = DbConfig()


class UserFieldValue(db_config.Base):
    __tablename__ = 'user_field_value'

    id = Column(Integer, primary_key=True)
    user_field_id = Column(Integer, ForeignKey('user_field.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    value = Column(Integer, nullable=False)

    user_field = relationship('UserField')