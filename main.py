# системные импорты
import os, datetime, json
from functools import cached_property
from flask_babel import Babel
from dotenv import load_dotenv
from peewee import OperationalError
from flask import redirect
# импорт моделей
from Models.Builds_authors import *
from Models.Builds_hardwares import *
from Models.Builds import *
from Models.GalleryEvents_images import *
from Models.GalleryEvents import *
from Models.Hardwares import *
from Models.Faq import *
from Models.Images import *
from Models.News import *
from Models.Persons_types import *
from Models.Persons import *
from Models.Roles import *
from Models.Schedule import *
from Models.Sliders import *
from Models.Statistics import *
from Models.Users import *
# импортирование flask_admin переопределений моделей 
from Models.ModelView.Builds_admin import * 
from Models.ModelView.Builds_hardwares_admin import *
from Models.ModelView.Builds_authors_admin import *
from Models.ModelView.GalleryEvents_admin import *
from Models.ModelView.GalleryEvents_images_admin import *
from Models.ModelView.Hardwares_admin import *
from Models.ModelView.Faq_admin import *
from Models.ModelView.Images_admin import *
from Models.ModelView.News_admin import *
from Models.ModelView.Persons_admin import *
from Models.ModelView.Persons_types_admin import *
from Models.ModelView.Roles_admin import *
from Models.ModelView.Schedule_admin import *
from Models.ModelView.Sections_admin import *
from Models.ModelView.Sliders_admin import *
from Models.ModelView.Statistics_admin import *
from Models.ModelView.Users_admin import *
# импортирование блюпринтов
from blueprints.builds import builds_blueprint
from blueprints.gallary import gallery_blueprint
from blueprints.hardwares import hardwares_blueprint
from blueprints.index import index_blueprint
from blueprints.login import login_blueprint
from blueprints.news import news_blueprint
from blueprints.persons import persons_blueprint
from blueprints.schedule import schedule_blueprint
# импорт приложения фласк
from app import create_flaskApp
class App_controller():
    """класс реализующий стек фласк"""
    blueprints = [ # список всех шаблонов с маршрутами
            builds_blueprint,
            gallery_blueprint,
            hardwares_blueprint,
            index_blueprint,
            login_blueprint,
            news_blueprint,
            persons_blueprint,
            schedule_blueprint
            ]
    root = os.path.dirname(__file__)
    """класс для функций и данных приложения"""
    def __init__(self):
        self._tempImg = [r'static', r'temp', r'img']
        self._webpImg = [r'static', r'webp'] 
    @cached_property
    def tempImg(self):
        """геттер пути temp для картинок"""
        return os.path.join(*self._tempImg)
    @cached_property
    def webpImg(self):
        """геттер пути webp для веб-картинок"""
        return os.path.join(*self._webpImg)
    @staticmethod
    def get_flaskApp():
        return create_flaskApp()
    @classmethod
    def get_osPath(cls, *args):
        return os.path.join(cls.root, *args)
    @staticmethod
    def open_file(src):
        """читает файл и возвращает результат, упрощает общий вид кода"""
        try:
            with open(src, 'r') as file:
                return file.read()
        except:
            print('ошибка чтения файла: ', src)
    @staticmethod
    def make_Dir(src):
        """проверка директории, если таковой нет то создает ее"""
        try:
            if os.path.isdir(src) != True:
                os.mkdir(src) # переделать под Path(src).mkdir(parents=True, exist_ok=True)
            return src
        except:
            print('ошибка создания папки')
    @staticmethod
    def make_recurDirs(src):
        # """проверка директории, если таковой нет то создает ее"""
        try:
            if os.path.isdir(src) != True:
                os.makedirs(src, exist_ok=True)
            return src    
        except:
            print('ошибка создания рекурсивно несколько папок')
    @staticmethod
    def get_curDate():
        return str(datetime.datetime.today().strftime('%Y-%m-%d').replace('-', '_'))
    @staticmethod
    def countListdir(src):
        return str(len(os.listdir(src)))
    def make_categoryDir(self, category):
        savePath = self.make_recurDirs(os.path.join(self.webpImg, self.get_curDate(), category)) # создаем папки
        cur_dir_name = category + self.countListdir(savePath) # нумеруем категорию
        return self.make_Dir(os.path.join(savePath, cur_dir_name))
    @staticmethod
    def models_importer():
        # для моделей без класс представления flask-admin необходима оболочка
        #  [ModelView(model) for model in models] 
        return [
            Builds_admin(Builds),
            Builds_hardwares_admin(Builds_hardwares),
            Builds_authors_admin(Builds_authors),
            GalleryEvents_admin(GalleryEvents),
            GalleryEvents_images_admin(GalleryEvents_images),
            Hardwares_admin(Hardwares),
            Faq_admin(Faq),
            Images_admin(Images),
            News_admin(News),
            Persons_admin(Persons),
            Persons_types_admin(Persons_types),
            Roles_admin(Roles),
            Schedule_admin(Schedule),
            
            Statistics_admin(Statistics),
            Users_admin(Users),
            Sliders_admin(Sliders)
        ]
    @classmethod
    def registerAll_blueprints(cls, app):
        for blueprint in cls.blueprints:
            app.register_blueprint(blueprint)   

if __name__ == '__main__':
    app = App_controller.get_flaskApp()
    app.secret_key = 'jksdhf l;lkj&*~19273l;kaszdfop['
    
    # определения языка приложения
    def get_locale():
        return 'ru'
    babel = Babel(app, locale_selector=get_locale) # аргумент требует функцию

    App_controller.registerAll_blueprints(app=app)
    @app.context_processor
    def inject_db_status():
        # Проверяем, сидим ли мы на заглушке
        db_is_fake = isinstance(db.obj, SqliteDatabase)
        return {'db_is_fake': db_is_fake}
    # вытягиваем конфигурацию списка моделей в админ панели
    @app.context_processor
    def nav_config_admin():
        path =  App_controller.get_osPath('static','config','json', 'nav_config.json')
        with open(path, 'r', encoding="utf-8") as config_file:
            nav_config = json.load(config_file)
        return {'nav_config': nav_config}
    @app.context_processor
    def env_sql_db_data():
        root = os.path.dirname(__file__)
        env_path = os.path.join(root, 'static', 'config', 'db.env')
        load_dotenv(env_path, override=True)
        return {'db_data' : {
            'name' : os.getenv('name'),
            'ip' : os.getenv('ip'),
            'port' : os.getenv('port')
                }
            } 
    # @app.context_processor
    # def db_is_ready_context():
    #     global db_is_ready
    #     return {'init_db_status' : db_is_ready}
     
    from peewee import OperationalError
    @app.errorhandler(OperationalError)
    def handle_db_error(e):
        # При ошибке БД перенаправляем в админку (где обычно показывается форма подключения)
        return redirect('/admin')
    app.run(debug=True)
    

    
