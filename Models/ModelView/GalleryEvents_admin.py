from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class GalleryEvents_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Галереи'
        super().__init__(model, *args, **kwargs)
    column_labels = {
        'date' : 'дата',
        'title' : 'заголовок',
    }
#     """
#     модель 
#     """
#     id = PrimaryKeyField()
#     date = DateField()
#     title = CharField()
# if __name__ == '__main__':
#     connect_db().create_tables([GalleryEvents])