from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from schema.UserGroupSchema import UserGroupSchema
from schema.UserFieldValueSchema import UserFieldValueSchema

from model.User import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_relationships = True

    values = fields.Nested(UserFieldValueSchema, many=True)
    group = fields.Nested(UserGroupSchema, many=False)