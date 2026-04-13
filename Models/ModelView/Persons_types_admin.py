# импорты
from Models.ModelView.BaseModelView import BaseModelView
class Persons_types_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Типы персон'
    uses_upload = False
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        self.form_extra_fields = {}
        super().__init__(model, modelTableName, *args, **kwargs)
    # форматируем столбцы из данных модели и обратных связей
    column_labels = {
        'type' : 'Тип персоны',
        }
    
    