"""файл для тестирования модулей и обхода ошибок поиска vs code"""
from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
from Models.TableBlocks import TableBlocks
from Models.Schedule import Schedule
from Models.Sections import Tables
class Tables(Base):
    """
    модель таблиц в системе
    """
    id = PrimaryKeyField()
    titleName = CharField()
    tableDesc = TextField()
    tableReq = CharField()
    tableBlock_id = ForeignKeyField(TableBlocks)
if __name__ == '__main__':
    connect_db().create_tables([Tables])