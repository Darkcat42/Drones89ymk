from peewee import PrimaryKeyField, ForeignKeyField
from Models.Base import *
from Models.Persons import Persons
from Models.Builds import Builds
class Builds_authors(Base):
    """
    модель 
    """
    id = PrimaryKeyField()
    persons_id = ForeignKeyField(Persons)
    builds_id = ForeignKeyField(Builds)
    
if __name__ == '__main__':
    connect_db().create_tables([Builds_authors, Persons, Builds])