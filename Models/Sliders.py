from peewee import PrimaryKeyField
from Models.Base import *
from Models.Images import *
from Models.GalleryEvents import *
from disable.Sections import *
class Sliders(Base):
    """модель для слайдеров"""
    id = PrimaryKeyField()
    name = CharField()


