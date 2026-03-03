import os, datetime
from functools import cached_property
class App_contorller():
    """класс для функций и данных приложения"""
    def __init__(self):
        self._rootDir = __file__
        self._tempImg = [r'static', r'temp', r'img']
        self._webpImg = [r'static', r'webp'] 
    @cached_property
    def rootDir(self):
        return os.path.dirname(os.path.realpath(__file__))
    @cached_property
    def tempImg(self):
        """геттер пути temp для картинок"""
        return os.path.join(self.rootDir, *self._tempImg)
    @cached_property
    def webpImg(self):
        """геттер пути webp для веб-картинок"""
        return os.path.join(self.rootDir, *self._webpImg)
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
                os.mkdir(src)
            return src
        except:
            print('ошибка создания папки')
    @staticmethod
    def make_recurDirs(src):
        # """проверка директории, если таковой нет то создает ее"""
        try:
            if os.path.isdir(src) != True:
                os.makedirs(src)
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
        print(cur_dir_name)
        print(savePath)
        print(cur_dir_name)
        return self.make_Dir(os.path.join(savePath, cur_dir_name))
    
