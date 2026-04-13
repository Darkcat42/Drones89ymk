# импорты
from Models.ModelView.BaseModelView import BaseModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html

class GalleryEvents_images_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Галереи и картинки'
    uses_upload = False
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
    def _image_formatter(view, context, model, name):
        image_src = model.image_id.src
        if not image_src:
            return ""
        return Markup(f'<img src="../../{image_src}" class="img-fluid fsi lazy" alt="...">')
    def _galleryEvent_title_formatter(view, context, model, name):
        galleryEvent_title = model.galleryEvent_id.title
        if not galleryEvent_title:
            return ""
        return Markup(f'<a href="/admin/galleryevents/">{galleryEvent_title}</a>')
    # форматируем сами столбцы
    column_labels = {   
        'galleryEvent_id' : 'галерея',
        'image_id' : 'картинка',
    }
    # форматируем значения в таблице, если нет то None для логики генератора словаря
    formatter_list = [
        _galleryEvent_title_formatter,
        _image_formatter]

