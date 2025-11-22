from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class Images(Base):
    """
    модель таблицы изображения
    """
    id = PrimaryKeyField()
    filename = CharField()
    src = TextField()
    alt = TextField()
if __name__ == '__main__':
    connect_db().create_tables([Images])