# импорты
from Models.ModelView.BaseModelView import BaseModelView
class Sections_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Секции'
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)


    


