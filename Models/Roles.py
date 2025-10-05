#класс для таблицы пользователей в бд
from Models.Base import *
class Roles(Base):
    id = PrimaryKeyField()
    role = CharField()
if __name__ == '__main__':
    connect_db().create_tables([Roles])