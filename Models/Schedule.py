from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class Schedule(Base):
    """
    модель веб-страниц, которые
    содержат внешние ключи на блоки данных, которые
    содержат заголовки, картинки, текста и тп
    """
    id = PrimaryKeyField()
    location = CharField()
    day = CharField()
    start = CharField()
    end = CharField()
if __name__ == '__main__':
    connect_db().create_tables([Schedule])