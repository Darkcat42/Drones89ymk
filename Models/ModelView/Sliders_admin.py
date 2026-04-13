# импорты
from Models.ModelView.BaseModelView import BaseModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html

class Sliders_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Слайдеры'
    uses_upload = True
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
    def _image_formatter(view, context, model, name):
        image_src = model.image_id.src
        if not image_src:
            return ""
        return Markup(f'<img src="../../{image_src}" class="img-fluid fsi lazy" alt="...">')
    # форматируем сами столбцы
    column_labels = {
        'image_id' : 'картинка',
        'name' : 'Название слайдера',
    }
    column_formatters = {
        'image_id': _image_formatter,
    }
    

