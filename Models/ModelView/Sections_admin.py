from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Sections_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Секции'
        super().__init__(model, *args, **kwargs)
#     """
#     модель таблиц в системе
#     """
#     id = PrimaryKeyField()
#     sectionName = CharField()
#     sectionTitle = CharField()
#     sectionDesc = TextField()
#     sectionReq = CharField()
# if __name__ == '__main__':
#     connect_db().create_tables([Sections])

    


