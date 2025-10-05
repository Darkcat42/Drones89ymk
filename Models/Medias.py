#класс для таблицы пользователей в бд
from Models.Samples import Samples
from peewee import ForeignKeyField
from Models.Base import *
class Paragraphs(Base):
    id = PrimaryKeyField()
    type = CharField()
    src = CharField()
    sample_id = ForeignKeyField(Samples)
if __name__ == '__main__':
    connect_db().create_tables([Paragraphs])