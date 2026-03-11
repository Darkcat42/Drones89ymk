from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Users_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Пользователи'
        super().__init__(model, *args, **kwargs)
#     """
#     модель пользователей системы
#     """
#     id = PrimaryKeyField()
#     FIO = CharField()
#     login = CharField()
#     password = CharField()
#     role_id = ForeignKeyField(Roles, backref='role_id')
# if __name__ == '__main__':
#     connect_db().create_tables([Users, Roles])