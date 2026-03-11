from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Hardwares_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Оборудование'
        super().__init__(model, *args, **kwargs)
#     """
#     модель 
#     """
#     id = PrimaryKeyField()
#     category = CharField()
#     name = CharField()
#     count = IntegerField()
#     cost = IntegerField()
#     sourceName = TextField()
#     sourceUrl = CharField()
# if __name__ == '__main__':
#     connect_db().create_tables([Hardwares])