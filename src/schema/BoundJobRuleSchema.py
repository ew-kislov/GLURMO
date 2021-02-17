from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from .JobRuleSchema import JobRuleSchema
from ..model.BoundJobRule import BoundJobRule


class BoundJobRuleSchema(SQLAlchemySchema):
    id = auto_field()
    job_rule_id = auto_field()
    user_id = auto_field()
    user_group_id = auto_field()
    scheduler_partition_id = auto_field()
    priority = auto_field()
    is_default = auto_field()
    is_active = auto_field()

    class Meta:
        model = BoundJobRule
        load_instance = True
        include_relationships = True

    job_rule = fields.Nested(JobRuleSchema)