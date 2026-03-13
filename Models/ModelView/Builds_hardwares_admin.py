from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Builds_hardwares_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Сборки и оборудование'
        super().__init__(model, *args, **kwargs)
    column_labels = {
        'Hardwares_id' : 'оборудование',
        'builds_id' : 'сборка',
    }
#     """
#     модель 
#     """
#     id = PrimaryKeyField()
#     Hardwares_id = ForeignKeyField(Hardwares)
#     builds_id = ForeignKeyField(Builds)
    
# if __name__ == '__main__':
#     connect_db().create_tables([Builds_hardwares, Hardwares, Builds])