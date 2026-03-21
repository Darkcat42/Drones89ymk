from peewee import PrimaryKeyField, CharField, ForeignKeyField
from Models.Base import *
from Models.Persons_types import Persons_types
from Models.Images import Images
class Persons(Base):
    """модель для персон"""
    id = PrimaryKeyField()
    persons_types_id = ForeignKeyField(Persons_types, backref='persons_types_id')
    images_id = ForeignKeyField(Images)
    firstName = CharField()
    lastName = CharField()
    person_desc = TextField()

    def __str__(self):
        return self.firstName +' '+ self.lastName
    
if __name__ == '__main__':
    connect_db().create_tables([Persons, Persons_types, Images])