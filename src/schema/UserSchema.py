from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from .UserGroupSchema import UserGroupSchema
from .UserFieldValueSchema import UserFieldValueSchema

from ..model.User import User

class UserSchema(SQLAlchemySchema):
    id = auto_field()
    name = auto_field()
    uid = auto_field()
    is_admin = auto_field()
    
    class Meta:
        model = User
        load_instance = True
        include_relationships = True

    values = fields.Nested(UserFieldValueSchema, many=True)
    group = fields.Nested(UserGroupSchema, many=False)