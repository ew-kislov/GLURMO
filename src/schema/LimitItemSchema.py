from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from .UserFieldSchema import UserFieldSchema
from ..model.LimitItem import LimitItem


class LimitItemSchema(SQLAlchemySchema):
    id = auto_field()
    max_value = auto_field()

    class Meta:
        model = LimitItem
        load_instance = True
        include_relationships = True

    user_field = fields.Nested(UserFieldSchema)