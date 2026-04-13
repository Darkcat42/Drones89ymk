"""модуль для подлючения к базе данных"""
from peewee import *
import os
from dotenv import load_dotenv
db = Proxy()
db.initialize(SqliteDatabase(':memory:'))  # Заглушка на случай отсутствия MySQL
db_is_ready = False
def init_db():
    global db_is_ready
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(root, 'static', 'config', 'db.env')
    load_dotenv(env_path, override=True)
    try:
        global db_is_ready
        # Пытаемся создать объект базы
        new_db = MySQLDatabase(
            os.getenv('name'),
            user=os.getenv('login'),
            password=os.getenv('passwd'),
            host=os.getenv('ip'),
            port=int(os.getenv('port', 3306)),
            connect_timeout=3 # СТАВИМ ТАЙМАУТ 3 секунды, чтобы не висело вечно
        )
        # Проверяем соединение перед присвоением прокси
        conn = new_db.connection()
        conn.close()
        db.initialize(new_db)
        db_is_ready = True
        return True
    except:
        print(f"Ошибка подключения к БД")
        db.initialize(SqliteDatabase(':memory:'))
        db_is_ready = False
        return False

def reload_db():
    """Переподключение после обновления .env (вызывается из формы)."""
    global db, db_is_ready
    if not db.is_closed():
        db.close()
    db.initialize(SqliteDatabase(':memory:'))
    return init_db()


