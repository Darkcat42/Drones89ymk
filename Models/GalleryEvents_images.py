from peewee import PrimaryKeyField, IntegerField, CharField, TextField
from Models.Base import *
from Models.Images import *
from Models.GalleryEvents import *
class GalleryEvents_images(Base):
    """модель многие ко многим для галерей и картинок"""
    id = PrimaryKeyField()
    image_id = ForeignKeyField(Images, backref='image_id')
    galleryEvent_id = ForeignKeyField(GalleryEvents, backref='galleryEvent_id')

