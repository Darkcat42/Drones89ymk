from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
from Models.Base import *
from Models.Sections import Sections
class Webpages(Base):
    """
    модель веб-страниц, которые 
    содержат внешние ключи на блоки данных, которые
    содержат заголовки, картинки, текста и тп
    """
    id = PrimaryKeyField()
    name = CharField()
    sections_id = ForeignKeyField(Sections)
if __name__ == '__main__':
    connect_db().create_tables([Webpages, Sections])