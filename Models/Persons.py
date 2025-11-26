from peewee import PrimaryKeyField, CharField, ForeignKeyField
from Models.Base import *
from Models.Persons_types import Persons_types
from Models.Images import Images
class Persons(Base):
    """
    модель 
    """
    id = PrimaryKeyField()
    persons_types_id = ForeignKeyField(Persons_types)
    images_id = ForeignKeyField(Images)
    firstName = CharField()
    lastName = CharField()
    person_desc = TextField()
    
if __name__ == '__main__':
    connect_db().create_tables([Persons, Persons_types, Images])