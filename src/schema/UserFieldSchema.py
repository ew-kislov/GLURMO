from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from ..model.UserField import UserField


class UserFieldSchema(SQLAlchemySchema):
    id = auto_field()
    name = auto_field()

    class Meta:
        model = UserField
        load_instance = True
        include_relationships = True