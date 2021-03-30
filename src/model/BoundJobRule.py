from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from .UserField import UserField

from ..config.DbConfig import DbConfig

db_config = DbConfig()


class BoundJobRule(db_config.Base):
    __tablename__ = 'bound_job_rule'

    id = Column(Integer, primary_key=True)
    job_rule_id = Column(Integer, ForeignKey('job_rule.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user_group_id = Column(Integer, ForeignKey('user_group.id'))
    scheduler_partition_id = Column(Integer, ForeignKey('scheduler_partition.id'))
    priority = Column(Integer, nullable=True)
    is_default = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    creation_date = Column(DateTime, nullable=False)

    job_rule = relationship('JobRule')
    user = relationship('User')