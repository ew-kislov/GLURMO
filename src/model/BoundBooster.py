from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from .UserField import UserField

from ..config.DbConfig import DbConfig

db_config = DbConfig()


class BoundBooster(db_config.Base):
    __tablename__ = 'bound_booster'

    id = Column(Integer, primary_key=True)
    booster_id = Column(Integer, ForeignKey('booster.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    amount = Column(Boolean, nullable=False)
    creation_date = Column(DateTime, nullable=False)

    booster = relationship('Booster')