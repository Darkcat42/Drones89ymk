from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class GalleryEvents(Base):
    """
    модель 
    """
    id = PrimaryKeyField()
    date = DateField()
    title = CharField()
if __name__ == '__main__':
    connect_db().create_tables([GalleryEvents])