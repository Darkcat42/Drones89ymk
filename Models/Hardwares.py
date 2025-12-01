from peewee import PrimaryKeyField, CharField
from Models.Base import *
class Hardwares(Base):
    """
    модель 
    """
    id = PrimaryKeyField()
    category = CharField()
    name = CharField()
    count = IntegerField()
    cost = IntegerField()
    sourceName = TextField()
    sourceUrl = CharField()
if __name__ == '__main__':
    connect_db().create_tables([Hardwares])