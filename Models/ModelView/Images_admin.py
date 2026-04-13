# импорты
from Models.ModelView.BaseModelView import BaseModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Images_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Картинки'
    uses_upload = True
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)       
    def _image_formatter(view, context, model, name):
        image_src = model.src
        src = url_for('static', filename='webp/' + str(image_src))
        return Markup(f'<img src="{src}" class="w-100 lazy" loading="lazy" alt="...">')
    # форматируем сами столбцы
    column_labels = {
        'src' : 'файл',
        'alt' : 'подпись картинки',
        'prev' : 'картинка',
    }
    formatter_list = [
        None,
        None,
        _image_formatter
    ]
