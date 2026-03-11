from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Persons_types_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
            if 'name' not in kwargs:
                kwargs['name'] = 'Типы персон'
            super().__init__(model, *args, **kwargs)
#     """
#     модель 
#     """
#     id = PrimaryKeyField()
#     type = CharField()
    
# if __name__ == '__main__':
#     connect_db().create_tables([Persons_types])