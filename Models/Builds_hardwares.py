from peewee import PrimaryKeyField, ForeignKeyField
from Models.Base import *
from Models.Hardwares import Hardwares
from Models.Builds import Builds
class Builds_hardwares(Base):
    """модель многие ко многим для сборок и оборудования"""
    id = PrimaryKeyField()
    count = IntegerField()
    hardwares_id = ForeignKeyField(Hardwares)
    # backref используется для обратной связи внешних ключей
    builds_id = ForeignKeyField(Builds, backref='hardwares')
    @property
    def safe_hardwares_id(self):
        try:
            return self.hardwares_id.id
        except:
            return False
    @property
    def safe_builds_id(self):
        try:
            return self.builds_id.id
        except:
            return False
    

    
    
