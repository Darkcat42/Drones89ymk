from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
from Models.Images import *
from Models.GalleryEvents import *
class GalleryEvents_images(Base):
    """
    модель таблицы изображения
    """
    id = PrimaryKeyField()
    image_id = ForeignKeyField(Images, backref='image_id')
    galleryEvent_id = ForeignKeyField(GalleryEvents, backref='galleryEvent_id')

if __name__ == '__main__':
    connect_db().create_tables([GalleryEvents_images, Images, GalleryEvents])
