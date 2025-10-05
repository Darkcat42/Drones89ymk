#класс для таблицы пользователей в бд
from peewee import PrimaryKeyField, CharField, ForeignKeyField
from flask_login import UserMixin
from Models.Base import *
from Models.Roles import Roles
class Users(Base, UserMixin):
    id = PrimaryKeyField()
    FIO = CharField()
    login = CharField()
    password = CharField()
    role = ForeignKeyField(Roles, backref='role')
if __name__ == '__main__':
    connect_db().create_tables([Users, Roles])