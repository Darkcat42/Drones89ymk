from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Sliders_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Слайдеры'
        super().__init__(model, *args, **kwargs)
#     id = PrimaryKeyField()
#     image_id = ForeignKeyField(Images, backref='image_id')

# if __name__ == '__main__':
#     connect_db().create_tables([Sliders, Images])
