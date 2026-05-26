# это базовый класс для всех моделей системы
from connection.connect import *
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
class Base(Model):
    def __getattribute__(self, name):
        try:
            # Вызываем стандартный механизм получения атрибута
            return super().__getattribute__(name)
        except DoesNotExist:
            # Если Peewee не нашел запись в связанной таблице — возвращаем None
            # Вместо того, чтобы ронять всё приложение
            return Markup('<p data-Peewee-Attr-Error=true>ошибка атрибута модели БД</p>')
    """базовый класс для моделей базы данных"""
    @classmethod
    def create_tables_db(cls):
        if db_is_ready and not isinstance(db.obj, SqliteDatabase):
            db.create_tables([cls])

    @classmethod
    def ensure_tables(cls):
        """Вызывается после успешного подключения для создания всех таблиц."""
        if db_is_ready:
            # импорт моделей
            from Models.Builds_authors import Builds_authors
            from Models.Builds_hardwares import Builds_hardwares
            from Models.Builds import Builds
            from Models.GalleryEvents_images import GalleryEvents_images
            from Models.GalleryEvents import GalleryEvents
            from Models.Hardwares import Hardwares
            from Models.Faq import Faq
            from Models.Images import Images
            from Models.News import News
            from Models.Persons_types import Persons_types
            from Models.Persons import Persons
            from Models.Roles import Roles
            from Models.Schedule import Schedule
            from Models.Sliders import Sliders
            from Models.Statistics import Statistics
            from Models.Users import Users
            # импортировать все модели вручную или автоматически собрать подклассы Base
            models = [
                Builds_authors,
                Builds_hardwares,
                Builds,
                GalleryEvents_images,
                GalleryEvents,
                Hardwares,
                Faq,
                Images,
                News,
                Persons_types,
                Persons,
                Roles,
                Schedule,
                Sliders,
                Statistics,
                Users]  # дополните полным списком ваших моделей
            db.create_tables(models, safe=True)
            
    class Meta:
        database = db


