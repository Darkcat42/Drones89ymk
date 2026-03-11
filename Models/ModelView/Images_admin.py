from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Images_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
            if 'name' not in kwargs:
                kwargs['name'] = 'Картинки'
            super().__init__(model, *args, **kwargs)
#     """
#     модель таблицы изображения
#     """
#     id = PrimaryKeyField()
#     filename = CharField()
#     src = TextField()
#     alt = TextField()
# if __name__ == '__main__':
#     connect_db().create_tables([Images])
    