from peewee import PrimaryKeyField, ForeignKeyField
from Models.Base import *
from Models.Hardwares import Hardwares
from Models.Builds import Builds
class Builds_hardwares(Base):
    """
    модель 
    """
    id = PrimaryKeyField()
    Hardwares_id = ForeignKeyField(Hardwares)
    builds_id = ForeignKeyField(Builds)
    
if __name__ == '__main__':
    connect_db().create_tables([Builds_hardwares, Hardwares, Builds])