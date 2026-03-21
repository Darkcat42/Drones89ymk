from peewee import PrimaryKeyField, CharField
from Models.Base import *
class Schedule(Base):
    """модель для расписания"""
    id = PrimaryKeyField()
    location = CharField()
    day = CharField()
    start = CharField()
    end = CharField()
if __name__ == '__main__':
    connect_db().create_tables([Schedule])