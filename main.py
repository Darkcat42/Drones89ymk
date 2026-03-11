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
from Models.Sections import *
from Models.Users import *
from Models.Videos import *
from Models.Webpages import *

# импортирование flask_admin переопределений моделей  
from Models.ModelView.Builds_authors_admin import Builds_authors_admin

import os, datetime
from functools import cached_property
import peewee
from flask_admin.contrib.peewee import ModelView

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
            Builds_authors_admin(Builds_authors)
        ]
        
            

    

    
