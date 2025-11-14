from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
from Models.Schedule import Schedule_table
class Sections(Base):
    """
    модель веб-страниц, которые
    содержат внешние ключи на блоки данных, которые
    содержат заголовки, картинки, текста и тп
    """
    id = PrimaryKeyField()
    name = CharField()
    schedule_table_id  = ForeignKeyField(Schedule_table)
if __name__ == '__main__':
    connect_db().create_tables([Sections, Schedule_table])