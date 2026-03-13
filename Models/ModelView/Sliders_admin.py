from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Sliders_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Слайдеры'
        super().__init__(model, *args, **kwargs)
    def _image_formatter(view, context, model, name):
        image_src = model.image_id.src
        if not image_src:
            return ""
        return Markup(f'<img src="../../{image_src}" class="img-fluid fsi lazy" alt="...">')
    # форматируем сами столбцы
    column_labels = {
        'image_id' : 'картинка',
    }
    column_formatters = {
        'image_id': _image_formatter,
    }

