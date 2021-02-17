from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from .LimitItemSchema import LimitItemSchema
from ..model.BoundLimit import BoundLimit


class BoundLimitSchema(SQLAlchemySchema):
    id = auto_field()
    limit_id = auto_field()
    user_id = auto_field()
    user_group_id = auto_field()
    scheduler_partition_id = auto_field()
    refresh_period_days = auto_field()
    priority = auto_field()
    is_default = auto_field()
    is_active = auto_field()

    class Meta:
        model = BoundLimit
        load_instance = True
        include_relationships = True

    limit_item = fields.Nested(LimitItemSchema)