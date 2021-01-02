from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from schema.UserFieldSchema import UserFieldSchema
from model.UserFieldValue import UserFieldValue


class UserFieldValueSchema(SQLAlchemySchema):
    value = auto_field()

    class Meta:
        model = UserFieldValue
        load_instance = True
        include_relationships = True

    user_field = fields.Nested(UserFieldSchema)