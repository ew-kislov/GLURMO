from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from ..model.UserField import UserField

from ..config.DbConfig import DbConfig

db_config = DbConfig()


class Booster(db_config.Base):
    __tablename__ = 'booster'

    id = Column(Integer, primary_key=True)
    soft_priority_increase = Column(Integer, nullable=True)
    hard_priority_increase = Column(Integer, nullable=True)
    period_minutes = Column(Integer, nullable=False)
    creation_date = Column(DateTime, nullable=False)