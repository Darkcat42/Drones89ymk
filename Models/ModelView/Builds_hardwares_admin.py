# импорты
from Models.ModelView.BaseModelView import BaseModelView
class Builds_hardwares_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Сборки и оборудование'
    uses_upload = False
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
    def _hardware_formatter(view, context, model, name):
        return name
    # форматируем сами столбцы
    column_labels = {
        'Hardwares_id' : 'оборудование',
        'builds_id' : 'сборка',
    }
   
    formatter_list = [
        _hardware_formatter,
        None
    ]
