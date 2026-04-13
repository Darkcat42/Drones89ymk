from peewee import PrimaryKeyField, CharField
from Models.Base import *
from Models.Images import *
class Faq(Base):
    """модель для секции с вопросами и ответами"""
    id = PrimaryKeyField()
    question = CharField()
    answer = CharField()
