from peewee import PrimaryKeyField, ForeignKeyField
from Models.Base import *
from Models.Persons import Persons
from Models.Builds import Builds
class Builds_authors(Base):
    """модель многие ко многим для сборок и авторов"""
    id = PrimaryKeyField()
    persons_id = ForeignKeyField(Persons, backref='builds')
    builds_id = ForeignKeyField(Builds, backref='authors')
    # @property
    # def safe_persons_id(self):
    #     try:
    #         return self.persons_id.id
    #     except:
    #         return False
    # @property
    # def safe_builds_id(self):
    #     try:
    #         return self.builds_id.id
    #     except:
    #         return False
    
