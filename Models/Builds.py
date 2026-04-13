from peewee import PrimaryKeyField, CharField
from Models.Base import *
from Models.Images import *
class Builds(Base):
    """модель для сборок"""
    id = PrimaryKeyField()
    build_name = CharField()
    inch = CharField()
    build_desc = TextField()
    build_image_id = ForeignKeyField(Images)
    
