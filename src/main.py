import json
import datetime

from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, joinedload
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, fields, auto_field

from config.DbConfig import DbConfig

from model.User import User
from model.UserGroup import UserGroup
from model.UserField import UserField
from model.UserFieldValue import UserFieldValue

from schema.UserFieldSchema import UserFieldSchema
from schema.UserFieldValueSchema import UserFieldValueSchema
from schema.UserSchema import UserSchema
from schema.UserGroupSchema import UserGroupSchema

from http_server.server import run_server


db_config = DbConfig()
session = db_config.sesson_factory()

user_schema = UserSchema()

user = session.query(User).first()

dump_user = user_schema.dump(user)

print(json.dumps(dump_user, indent=4))

run_server()