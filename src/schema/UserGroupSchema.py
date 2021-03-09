from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from .UserFieldValueSchema import UserFieldValueSchema
from ..model.UserGroup import UserGroup

class UserGroupSchema(SQLAlchemySchema):
    id = auto_field()
    name = auto_field()
    
    class Meta:
        model = UserGroup
        load_instance = True
        include_relationships = True