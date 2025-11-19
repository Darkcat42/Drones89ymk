from Models.Base import *
class Roles(Base):
    """
    модель ролей для пользователей
    """
    id = PrimaryKeyField()
    role = CharField()
if __name__ == '__main__':
    connect_db().create_tables([Roles])