from Models.Builds_authors import *
from Models.Builds_hardwares import *
from Models.Builds import *
from Models.GalleryEvents_images import *
from Models.GalleryEvents import *
from Models.Hardwares import *
from Models.Images import *
from Models.News import *
from Models.Persons_types import *
from Models.Persons import *
from Models.Roles import *
from Models.Schedule import *
from Models.Users import *
from Models.Sliders import *
# импортирование блюпринтов
from blueprints.builds import builds_blueprint
from blueprints.gallary import gallery_blueprint
from blueprints.hardwares import hardwares_blueprint
from blueprints.index import index_blueprint
from blueprints.login import login_blueprint
from blueprints.news import news_blueprint
from blueprints.persons import persons_blueprint
from blueprints.schedule import schedule_blueprint
# импортирование flask_admin переопределений моделей 
from Models.ModelView.Builds_admin import Builds_admin 
from Models.ModelView.Builds_hardwares_admin import Builds_hardwares_admin
from Models.ModelView.Builds_authors_admin import Builds_authors_admin
from Models.ModelView.GalleryEvents_admin import GalleryEvents_admin
from Models.ModelView.GalleryEvents_images_admin import GalleryEvents_images_admin
from Models.ModelView.Hardwares_admin import Hardwares_admin
from Models.ModelView.Images_admin import Images_admin
from Models.ModelView.News_admin import News_admin
from Models.ModelView.Persons_admin import Persons_admin
from Models.ModelView.Persons_types_admin import Persons_types_admin
from Models.ModelView.Roles_admin import Roles_admin
from Models.ModelView.Schedule_admin import Schedule_admin
from Models.ModelView.Sections_admin import Sections_admin
from Models.ModelView.Users_admin import Users_admin
from Models.ModelView.Sliders_admin import Sliders_admin

import os, datetime
from functools import cached_property
class App_contorller():
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
            Images_admin(Images),
            News_admin(News),
            Persons_admin(Persons),
            Persons_types_admin(Persons_types),
            Roles_admin(Roles),
            Schedule_admin(Schedule),
            Sections_admin(Sections),
            Users_admin(Users),
            Sliders_admin(Sliders)
        ]
    @staticmethod
    def registerAll_blueprints(app):
        app.register_blueprint(builds_blueprint)
        app.register_blueprint(gallery_blueprint)
        app.register_blueprint(hardwares_blueprint)
        app.register_blueprint(index_blueprint)
        app.register_blueprint(login_blueprint)
        app.register_blueprint(news_blueprint)
        app.register_blueprint(persons_blueprint)
        app.register_blueprint(schedule_blueprint)
        
            

    

    
