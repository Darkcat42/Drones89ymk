from Models.Base import *
class Roles(Base):
    """модель ролей для пользователей"""
    id = PrimaryKeyField()
    role = CharField()
