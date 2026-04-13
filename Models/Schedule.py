from peewee import PrimaryKeyField, CharField
from Models.Base import *
class Schedule(Base):
    """модель для расписания"""
    id = PrimaryKeyField()
    location = CharField()
    day = CharField()
    start = CharField()
    end = CharField()
