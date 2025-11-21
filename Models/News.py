from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
from Models.Images import Images
class News(Base):
    """
    модель таблицы новости
    """
    id = PrimaryKeyField()
    title = CharField()
    news_desc = CharField()
    date = CharField()
    image_id = ForeignKeyField(Images)
if __name__ == '__main__':
    connect_db().create_tables([News, Images])