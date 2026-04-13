# импорты
from Models.ModelView.BaseModelView import BaseModelView
class Hardwares_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Оборудование'
    uses_upload = True
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
    # форматируем сами столбцы
    column_labels = {
        'galleryEvent_id' : 'галерея',
        'image_id' : 'картинка',
        'category': 'категория',
        'name': 'название',
        'count': 'количество',
        'cost': 'цена',
        'sourceName': 'источник',
        'sourceUrl': 'ссылка на источник'
    }
   