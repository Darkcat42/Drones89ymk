from peewee import PrimaryKeyField
from Models.Base import *
from Models.Images import *
from Models.GalleryEvents import *
class Sliders(Base):
    id = PrimaryKeyField()
    image_id = ForeignKeyField(Images, backref='image_id')

if __name__ == '__main__':
    connect_db().create_tables([Sliders, Images])
