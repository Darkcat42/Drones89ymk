from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class Images(Base):
    """модель для картинок"""
    id = PrimaryKeyField()
    # filename = CharField()
    src = TextField(null=True)
    alt = TextField()
