from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Roles_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
            if 'name' not in kwargs:
                kwargs['name'] = 'Роли пользователей'
            super().__init__(model, *args, **kwargs)
#     """
#     модель ролей для пользователей
#     """
#     id = PrimaryKeyField()
#     role = CharField()
# if __name__ == '__main__':
#     connect_db().create_tables([Roles])