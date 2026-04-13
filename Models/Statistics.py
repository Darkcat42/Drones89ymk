from peewee import PrimaryKeyField, CharField
from Models.Base import *
class Statistics(Base):
    """модель счета статистики на главной"""
    id = PrimaryKeyField()
    count = IntegerField()
    item = CharField()

  
