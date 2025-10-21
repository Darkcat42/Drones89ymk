from peewee import PrimaryKeyField, CharField, ForeignKeyField
from Models.Base import *
class Media_gallery(Base):
    id = PrimaryKeyField()
if __name__ == '__main__':
    connect_db().create_tables([Media_gallery])