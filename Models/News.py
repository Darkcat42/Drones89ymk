from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class News(Base):
    """
    модель таблицы новости
    """
    id = PrimaryKeyField()
    title = CharField()
    desc = CharField()
    img = CharField()
    date = CharField()
if __name__ == '__main__':
    connect_db().create_tables([News])