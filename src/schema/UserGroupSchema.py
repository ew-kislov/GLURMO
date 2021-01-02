from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from schema.UserFieldValueSchema import UserFieldValueSchema
from model.UserGroup import UserGroup

class UserGroupSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserGroup
        load_instance = True
        include_relationships = True