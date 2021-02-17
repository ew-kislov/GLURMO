from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from ..config.DbConfig import DbConfig

db_config = DbConfig()


class JobRule(db_config.Base):
    __tablename__ = 'job_rule'

    id = Column(Integer, primary_key=True)
    soft_priority = Column(Integer, nullable=True)
    soft_priority_period_minutes = Column(Integer, nullable=True)
    hard_priority = Column(Integer, nullable=True)
    creation_date = Column(DateTime, nullable=False)