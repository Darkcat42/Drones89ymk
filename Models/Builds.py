from peewee import PrimaryKeyField, CharField
from Models.Base import *
class Builds(Base):
    """
    модель 
    """
    id = PrimaryKeyField()
    inch = CharField()
    build_desc = TextField()
    
if __name__ == '__main__':
    connect_db().create_tables([Builds])