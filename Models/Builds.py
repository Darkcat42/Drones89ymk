from peewee import PrimaryKeyField, CharField
from Models.Base import *
from Models.Images import *
class Builds(Base):
    """
    модель 
    """
    id = PrimaryKeyField()
    inch = CharField()
    build_desc = TextField()
    build_image_id = ForeignKeyField(Images)
    
if __name__ == '__main__':
    connect_db().create_tables([Builds])