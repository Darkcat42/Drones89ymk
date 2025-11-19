from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
class Sections(Base):
    """
    модель таблиц в системе
    """
    id = PrimaryKeyField()
    sectionName = CharField()
    sectionTitle = CharField()
    sectionDesc = TextField()
    sectionReq = CharField()
if __name__ == '__main__':
    connect_db().create_tables([Sections])

    


