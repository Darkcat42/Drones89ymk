from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
from TableBlocks import TableBlocks
class Tables(Base):
    """
    модель веб-страниц, которые
    содержат внешние ключи на блоки данных, которые
    содержат заголовки, картинки, текста и тп
    """
    id = PrimaryKeyField()
    titleName = CharField()
    tableDesc = TextField()
    tableReq = CharField()
    tableBlock_id = ForeignKeyField(TableBlocks)
if __name__ == '__main__':
    connect_db().create_tables([Tables, TableBlocks])