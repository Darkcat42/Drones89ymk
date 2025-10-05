"""
модель веб-страниц, которые 
содержат внешние ключи на блоки данных, которые
содержат заголовки, картинки, текста и тп
"""
from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *

class Webpage(Base):
    id = PrimaryKeyField()
    name = CharField()
    url = TextField()
    type = CharField()
    position = IntegerField(default=0)
if __name__ == '__main__':
    connect_db().create_tables([Webpage])