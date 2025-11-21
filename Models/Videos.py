from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class Videos(Base):
    """
    модель таблицы изображения
    """
    id = PrimaryKeyField()
    src = TextField()
if __name__ == '__main__':
    connect_db().create_tables([Videos])