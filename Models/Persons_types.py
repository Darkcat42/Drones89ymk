from peewee import PrimaryKeyField, CharField
from Models.Base import *
class Persons_types(Base):
    """модель для типов персон"""
    id = PrimaryKeyField()
    type = CharField()
    
