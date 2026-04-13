# импорты
from Models.ModelView.BaseModelView import BaseModelView
class Roles_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Роли пользователей'
    uses_upload = False
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
    # форматируем столбцы из данных модели и обратных связей
    column_labels = {
        'role' : 'Роль пользователя',
        }