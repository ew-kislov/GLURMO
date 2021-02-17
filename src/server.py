import json
import datetime

from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, joinedload
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from .config.DbConfig import DbConfig

from .model import \
    User, UserGroup, UserField, UserFieldValue, SchedulerPartition, LimitItem, \
    BoundLimit, JobRule, BoundJobRule, Booster, BoundBooster

from .schema import \
    UserFieldSchema, UserFieldValueSchema, UserSchema, UserGroupSchema, SchedulerPartitionSchema, \
    LimitItemSchema, BoundLimitSchema, JobRuleSchema, BoundJobRuleSchema, BoosterSchema, BoundBoosterSchema

from .http_server.server import run_server

db_config = DbConfig()
session = db_config.sesson_factory()

# # user_schema = UserSchema()

# # user = session.query(User).first()

# # dump_user = user_schema.dump(user)

# # print(json.dumps(dump_user, indent=4))

# # bound_limit_schema = BoundLimitSchema()

# # bound_limits = session.query(BoundLimit).all()

# # dump_bound_limits = bound_limit_schema.dump(bound_limits, many=True)

# # print(json.dumps(dump_bound_limits, indent=4))

bound_limit_schema = BoundBoosterSchema()

bound_limits = session.query(BoundBooster).all()

dump_bound_limits = bound_limit_schema.dump(bound_limits, many=True)

print(bound_limits[1].id)

# run_server()