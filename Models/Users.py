from peewee import PrimaryKeyField, CharField, ForeignKeyField
from flask_login import UserMixin
from Models.Base import *
from Models.Roles import Roles
class Users(Base, UserMixin):
    """
    модель пользователей системы
    """
    id = PrimaryKeyField()
    FIO = CharField()
    login = CharField()
    password = CharField()
    role_id = ForeignKeyField(Roles, backref='role_id')
if __name__ == '__main__':
    connect_db().create_tables([Users, Roles])