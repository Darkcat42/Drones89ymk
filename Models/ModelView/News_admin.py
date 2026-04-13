# импорты
from Models.ModelView.BaseModelView import BaseModelView
from Controllers.ImagesController import *
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
from pathlib import Path
import os
class News_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Новости'
    uses_upload = True
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
    def _image_formatter(view, context, model, name):
        image_src = model.image_id.src
        src = url_for('static', filename='webp/' + str(image_src))
        return Markup(f'<img src="{src}" class="w-100 lazy" loading="lazy" alt="...">')
    column_labels = {
        'title' : 'заголовок',
        'news_desc' : 'текст новости',
        'date': 'дата новости',
        'image_id': 'Картинка',
    }
    formatter_list = [
        None,
        None,
        None,
        _image_formatter
    ]
    # # Скрываем стандартное поле связи с изображением
    form_excluded_columns = ('image_id')
    
    
    
    