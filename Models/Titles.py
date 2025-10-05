#класс для таблицы пользователей в бд
from Models.Samples import Samples
from peewee import ForeignKeyField
from Models.Base import *
class Titles(Base):
    id = PrimaryKeyField()
    title = CharField()
    position = IntegerField(default=0)
    sample_id = ForeignKeyField(Samples)
if __name__ == '__main__':
    connect_db().create_tables([Titles])