from peewee import PrimaryKeyField, ForeignKeyField
from Models.Base import *
from Models.Hardwares import Hardwares
from Models.Builds import Builds
class Builds_hardwares(Base):
    """модель многие ко многим для сборок и оборудования"""

    id = PrimaryKeyField()
    Hardwares_id = ForeignKeyField(Hardwares)
    # backref используется для обратной связи внешних ключей
    builds_id = ForeignKeyField(Builds, backref='hardwares')

    
    
