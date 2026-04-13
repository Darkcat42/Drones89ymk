from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class GalleryEvents(Base):
    """модель галерей"""
    id = PrimaryKeyField()
    date = DateField()
    title = CharField()
