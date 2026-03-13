from peewee import PrimaryKeyField, CharField
from Models.Base import *
from Models.Images import *
class Faq(Base):
    """
    модель 
    """
    id = PrimaryKeyField()
    question = CharField()
    answer = CharField()
    
if __name__ == '__main__':
    connect_db().create_tables([Faq])