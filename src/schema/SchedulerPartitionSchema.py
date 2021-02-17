from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from .UserFieldValueSchema import UserFieldValueSchema
from ..model.SchedulerPartition import SchedulerPartition

class SchedulerPartitionSchema(SQLAlchemyAutoSchema):
    id = auto_field()
    name = auto_field()
    
    class Meta:
        model = SchedulerPartition
        load_instance = True
        include_relationships = True