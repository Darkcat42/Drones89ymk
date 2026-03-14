from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class News_admin(ModelView):

    def __init__(self, model, *args, **kwargs):
            if 'name' not in kwargs:
                kwargs['name'] = 'Новости'
            super().__init__(model, *args, **kwargs)
    column_labels = {
        'title' : 'заголовок',
        'news_desc' : 'текст новости',
        'date': 'дата новости',
        'image_id': 'картинка'
    }
    def _image_formatter(view, context, model, name):
        image_src = model.image_id.src
        if not image_src:
            return ""
        return Markup(f'<img src="../../{image_src}" class="img-fluid fsi lazy" alt="...">')
    column_formatters = {
        'image_id': _image_formatter,
    }
    
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