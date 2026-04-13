from peewee import PrimaryKeyField, ForeignKeyField
from Models.Base import *
from Models.Persons import Persons
from Models.Builds import Builds
class Builds_authors(Base):
    """модель многие ко многим для сборок и авторов"""
    id = PrimaryKeyField()
    persons_id = ForeignKeyField(Persons, backref='builds')
    builds_id = ForeignKeyField(Builds, backref='authors')
    
