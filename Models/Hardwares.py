from peewee import PrimaryKeyField, CharField
from Models.Base import *
from Models.Images import *
class Hardwares(Base):
    """модель для оборудования"""
    id = PrimaryKeyField()
    category = CharField()
    name = CharField()
    count = IntegerField()
    cost = IntegerField()
    sourceName = TextField()
    sourceUrl = CharField()
    image_id = ForeignKeyField(Images) 
        
    def __str__(self):
        try:
            name = self.name
        except:
            name = 'Ошибка атрибута модели'
        return name
    
