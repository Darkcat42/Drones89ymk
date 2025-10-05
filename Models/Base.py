# это базовый класс для всех моделей системы
from connection.connect import *
class Base(Model):
    class Meta:
        database = connect_db()
