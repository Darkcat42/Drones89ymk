# импорты
from Models.ModelView.BaseModelView import BaseModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Images_models_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Картинки и модели'
    # uses_upload = True
    #     id = PrimaryKeyField()
    # model_name = CharField(null=True)
    # image_id = ForeignKeyField(Images, null=True)
    # row_id = IntegerField(null=True)
    
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)       

    # форматируем сами столбцы
    column_labels = {
        'model_name' : 'название модели',
        'image_id' : 'id картинки',
        'row_id' : 'id записи'
    }
    formatter_list = [
        None,
        None,
        None
    ]
