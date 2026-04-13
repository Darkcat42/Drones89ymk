# импорты
from Models.ModelView.BaseModelView import BaseModelView
class GalleryEvents_admin(BaseModelView):
    # название модели в списке админ панели
    list_template = 'admin/custom/GalleryEvents/list.html'
    modelTableName = 'Галереи'
    uses_upload = True
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
    # форматируем сами столбцы
    column_labels = {
        'date' : 'дата',
        'title' : 'заголовок',
    }
   