from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class GalleryEvents_images_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Галереи и картинки'
        super().__init__(model, *args, **kwargs)
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
    column_formatters = {
        'galleryEvent_id': _galleryEvent_title_formatter,
        'image_id': _image_formatter,
    }
    column_labels = {
        
        'galleryEvent_id' : 'галерея',
        'image_id' : 'картинка',
    }
#     """
#     модель таблицы изображения
#     """
#     id = PrimaryKeyField()
#     image_id = ForeignKeyField(Images, backref='image_id')
#     galleryEvent_id = ForeignKeyField(GalleryEvents, backref='galleryEvent_id')

# if __name__ == '__main__':
#     connect_db().create_tables([GalleryEvents_images, Images, GalleryEvents])
