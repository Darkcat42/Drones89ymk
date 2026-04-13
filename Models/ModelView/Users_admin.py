# импорты
from Models.ModelView.BaseModelView import BaseModelView
class Users_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Пользователи'
    uses_upload = False
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
    # список форматирований, порядок функций важен относительно столбцов 
    formatter_list = []
     # форматируем столбцы из данных модели и обратных связей
    column_labels = {
        'FIO' : 'ФИО',
        'login' : 'Логин',
        'password' : 'Пароль',
        'role_id' : 'Роль'}
