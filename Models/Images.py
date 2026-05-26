from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class Images(Base):
    """модель для картинок"""
    id = PrimaryKeyField()
    src = TextField(null=True)
    category = CharField()
    alt = TextField()
