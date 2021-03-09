from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from .BoosterSchema import BoosterSchema
from ..model.BoundBooster import BoundBooster


class BoundBoosterSchema(SQLAlchemySchema):
    id = auto_field()
    user_id = auto_field()
    amount = auto_field()

    class Meta:
        model = BoundBooster
        load_instance = True
        include_relationships = True

    booster = fields.Nested(BoosterSchema)