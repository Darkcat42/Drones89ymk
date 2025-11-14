from Models.Base import *
# from Models.old.Sections import Sections
class Webpages(Base):
    """
    модель веб-страниц, которые 
    содержат внешние ключи на блоки данных, которые
    содержат заголовки, картинки, текста и тп
    """
    id = PrimaryKeyField()
    name = CharField()
if __name__ == '__main__':
    connect_db().create_tables([Webpages])