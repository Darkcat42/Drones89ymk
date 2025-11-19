from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *



class Schedule(Base):
    """
    модель таблицы расписания
    """
    id = PrimaryKeyField()
    location = CharField()
    day = CharField()
    start = CharField()
    end = CharField()
if __name__ == '__main__':
    connect_db().create_tables([Schedule])