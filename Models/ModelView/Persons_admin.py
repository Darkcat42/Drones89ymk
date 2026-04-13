# импорты
from Models.ModelView.BaseModelView import BaseModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Persons_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Персоны'
    uses_upload = True
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
    def _image_formatter(view, context, model, name):
        image_src = model.image_id.src
        src = url_for('static', filename='webp/' + str(image_src))
        return Markup(f'<img src="{src}" class="w-100 lazy" loading="lazy" alt="...">')
    def _personType_formatter(view, context, model, name):
        persons_type = model.persons_types_id.type
        if not persons_type:
            return ""
        return Markup(f'<a href="/admin/persons_types/">{persons_type}</a>') 
    column_labels = {
        'persons_types_id' : 'тип персоны',
        'image_id' : 'картинка',
        'firstName': 'имя',
        'lastName': 'фамилия',
        'person_desc': 'описание персоны'
    }
    formatter_list = [
        _personType_formatter,
        _image_formatter,
    ]
    # # Скрываем стандартное поле связи с изображением
    form_excluded_columns = ('image_id')
    

