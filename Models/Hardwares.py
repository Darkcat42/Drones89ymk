from peewee import PrimaryKeyField, CharField
from Models.Base import *
class Hardwares(Base):
    """
    модель 
    """
    id = PrimaryKeyField()
    count = IntegerField()
    cost = IntegerField()
    source = CharField()
if __name__ == '__main__':
    connect_db().create_tables([Hardwares])