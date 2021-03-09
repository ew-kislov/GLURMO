from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from ..config.DbConfig import DbConfig

db_config = DbConfig()

class SchedulerPartition(db_config.Base):
    __tablename__ = 'scheduler_partition'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    creation_date = Column(DateTime, nullable=False)