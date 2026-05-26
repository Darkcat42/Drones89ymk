from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
from Models.Images import Images
class Images_models(Base):
    """модель для картинок и моделей М к М"""
    id = PrimaryKeyField()
    model_name = CharField(null=True)
    images_id = ForeignKeyField(Images, null=True)
    row_id = IntegerField(null=True)
