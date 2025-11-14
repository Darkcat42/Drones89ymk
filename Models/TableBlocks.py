from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
from Schedule import Schedule
class TableBlocks(Base):
    """
    модель веб-страниц, которые
    содержат внешние ключи на блоки данных, которые
    содержат заголовки, картинки, текста и тп
    """
    id = PrimaryKeyField()
    schedule = ForeignKeyField(Schedule)
if __name__ == '__main__':
    connect_db().create_tables([TableBlocks, Schedule])