from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from ..model.JobRule import JobRule


class JobRuleSchema(SQLAlchemySchema):
    id = auto_field()
    soft_priority = auto_field()
    soft_priority_period_minutes = auto_field()
    hard_priority = auto_field()

    class Meta:
        model = JobRule
        load_instance = True
        include_relationships = True