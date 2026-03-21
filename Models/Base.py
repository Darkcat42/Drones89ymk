# это базовый класс для всех моделей системы
from connection.connect import *
class Base(Model):
    """базовый класс для моделей базы данных"""
    @classmethod
    def create_tables_db(cls):
        connect_db().create_tables([cls])
    class Meta:
        database = connect_db()


