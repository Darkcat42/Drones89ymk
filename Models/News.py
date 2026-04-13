from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
from Models.Images import Images
class News(Base):
    """модель для новостей"""
    id = PrimaryKeyField()
    title = CharField()
    news_desc = CharField()
    date = CharField()
    image_id = ForeignKeyField(Images, backref='news')
