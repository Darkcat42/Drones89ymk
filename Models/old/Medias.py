from Models.old.Samples import Samples
from Models.Base import *
class Paragraphs(Base):
    id = PrimaryKeyField()
    type = CharField()
    src = CharField()
    sample_id = ForeignKeyField(Samples)
if __name__ == '__main__':
    connect_db().create_tables([Paragraphs])