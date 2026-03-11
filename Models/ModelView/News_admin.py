from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class News_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
            if 'name' not in kwargs:
                kwargs['name'] = 'Новости'
            super().__init__(model, *args, **kwargs)
    
#     """
#     модель таблицы новости
#     """
#     id = PrimaryKeyField()
#     title = CharField()
#     news_desc = CharField()
#     date = CharField()
#     image_id = ForeignKeyField(Images)
# if __name__ == '__main__':
#     connect_db().create_tables([News, Images])