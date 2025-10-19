from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class time_table(Base):
    """
    модель веб-страниц, которые
    содержат внешние ключи на блоки данных, которые
    содержат заголовки, картинки, текста и тп
    """
    id = PrimaryKeyField()
    title = CharField()
    location = CharField()
    day = CharField()
    start = CharField()
    end = CharField()
    requirements = CharField()
    description = TextField()
if __name__ == '__main__':
    connect_db().create_tables([time_table])