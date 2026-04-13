from peewee import PrimaryKeyField, CharField
from Models.Base import *
class Hardwares(Base):
    """модель для оборудования"""
    id = PrimaryKeyField()
    category = CharField()
    name = CharField()
    count = IntegerField()
    cost = IntegerField()
    sourceName = TextField()
    sourceUrl = CharField()

    def __str__(self):
        return self.name
