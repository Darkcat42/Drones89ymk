from peewee import PrimaryKeyField, CharField
from Models.Base import *
from Models.Images import *
class Builds(Base):
    """модель для сборок"""
    id = PrimaryKeyField()
    build_name = CharField()
    inch = CharField()
    build_desc = TextField()
    image_id = ForeignKeyField(Images) 
    @property
    def safe_image_id(self):
        try:
            return self.image_id.src
        except:
            return False
        
    
