from http_server.server import run_server
import json
import datetime

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, joinedload
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from config.DbConfig import DbConfig

from model.User import User
from model.UserField import UserField
from model.UserFieldValue import UserFieldValue


class UserFieldSchema(SQLAlchemySchema):
    id = auto_field()
    name = auto_field()

    class Meta:
        model = UserField
        load_instance = True
        include_relationships = True


class UserFieldValueSchema(SQLAlchemySchema):
    value = auto_field()

    class Meta:
        model = UserFieldValue
        load_instance = True
        include_relationships = True

    user_field = fields.Nested(UserFieldSchema)


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_relationships = True

    values = fields.Nested(UserFieldValueSchema, many=True)


db_config = DbConfig()
session = db_config.sesson_factory()

user_schema = UserSchema()

user = session.query(User).first()

dump_user = user_schema.dump(user)

print(json.dumps(dump_user, indent=4))

run_server()