from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Images_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
            if 'name' not in kwargs:
                kwargs['name'] = 'Картинки'
            super().__init__(model, *args, **kwargs)
    def _image_formatter(view, context, model, name):
        image_src = model.src
        if not image_src:
            return ""
        return Markup(f'<img src="../../{image_src}" class="img-fluid fsi lazy" alt="...">')
    # форматируем сами столбцы
    column_labels = {
        'filename' : 'файл',
        'src' : 'путь до файла',
        'alt' : 'подпись картинки',
        'prev' : Markup('<a href=''>картинка</a>'),
    }
    column_formatters = {
        'prev': _image_formatter,
    }
    column_list = {
        'filename',
        'prev',
        'src',
        'alt',
        
    }
#     """
#     модель таблицы изображения
#     """
#     id = PrimaryKeyField()
#     filename = CharField()
#     src = TextField()
#     alt = TextField()
# if __name__ == '__main__':
#     connect_db().create_tables([Images])
    