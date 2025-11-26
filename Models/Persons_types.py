from peewee import PrimaryKeyField, CharField
from Models.Base import *
class Persons_types(Base):
    """
    модель 
    """
    id = PrimaryKeyField()
    type = CharField()
    
if __name__ == '__main__':
    connect_db().create_tables([Persons_types])