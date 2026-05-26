# импорты
from Models.ModelView.BaseModelView import BaseModelView
from Controllers.ImagesController import *
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class News_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Новости'
    uses_multi_upload = True
    image_prev = True
    # uses_upload = True
    # inline_models = ((Images))
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)

    def _image_formatter(view, context, model, name):
        try:
            image_src = model.image_id.src
            src = url_for('static', filename=''+str(image_src))
            return Markup(f'<img src="{src}" class="img-fluid" alt="...">')
        except:
            return model.image_id
        #     src = ' '
        #     print(f'flask_admin > {model.__class__.__name__} > model view: ошибка получения изображения для новости')
        # return Markup('<p data-Peewee-Attr-Error=true>ошибка атрибута модели БД</p>')
    column_labels = {
        'title' : 'заголовок',
        'news_desc' : 'текст новости',
        'date': 'дата новости',
        'image_id': 'Превью',
    }
    formatter_list = [
        None,
        None,
        None,
        _image_formatter
    ]
    # # Скрываем стандартное поле связи с изображением
    form_excluded_columns = ('image_id')
    
    
    
    
    