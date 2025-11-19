from Models.Base import *
class Webpages(Base):
    """
    модель веб-страницы
    """
    id = PrimaryKeyField()
    name = CharField()
if __name__ == '__main__':
    connect_db().create_tables([Webpages])