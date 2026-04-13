# импорты
from Models.ModelView.BaseModelView import BaseModelView
class Schedule_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Расписание'
    uses_upload = False
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
    # форматируем сами столбцы
    column_labels = {
        'location' : 'Локация',
        'day' : 'День недели',
        'start' : 'начало занятий',
        'end' : 'конец занятий',
    }
