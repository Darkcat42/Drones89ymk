from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class Videos(Base):
    """модель для видеозаписей"""
    id = PrimaryKeyField()
    src = TextField()
