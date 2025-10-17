from Models.Base import *
class Samples(Base):
    id = PrimaryKeyField()
    name = CharField()
    html = TextField()
if __name__ == '__main__':
    connect_db().create_tables([Samples])