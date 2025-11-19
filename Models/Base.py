# это базовый класс для всех моделей системы
from connection.connect import *
class Base(Model):
    """
    базовый класс для моделей
    """
    class Meta:
        database = connect_db()
