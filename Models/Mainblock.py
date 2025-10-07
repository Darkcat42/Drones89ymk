
from peewee import PrimaryKeyField, IntegerField, CharField
from Models.Base import *
from Models.Samples import Samples
from Models.Webpage import Webpage 
from peewee import ForeignKeyField
class Mainblock(Base):
    id = PrimaryKeyField()
    html_name_id = CharField()
    title_id = IntegerField()
    paragraph_id = IntegerField()
    media_id = IntegerField()
    position = IntegerField(default=0)
    webpage_id = ForeignKeyField(Webpage)
    sample_id = ForeignKeyField(Samples)
if __name__ == '__main__':
    connect_db().create_tables([Mainblock])