from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class GalleryEvents_images_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Галереи и картинки'
        super().__init__(model, *args, **kwargs)
#     """
#     модель таблицы изображения
#     """
#     id = PrimaryKeyField()
#     image_id = ForeignKeyField(Images, backref='image_id')
#     galleryEvent_id = ForeignKeyField(GalleryEvents, backref='galleryEvent_id')

# if __name__ == '__main__':
#     connect_db().create_tables([GalleryEvents_images, Images, GalleryEvents])
