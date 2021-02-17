from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from ..model.Booster import Booster


class BoosterSchema(SQLAlchemySchema):
    id = auto_field()
    soft_priority_increase = auto_field()
    hard_priority_increase = auto_field()
    period_minutes = auto_field()

    class Meta:
        model = Booster
        load_instance = True
        include_relationships = True