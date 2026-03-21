# импорты 
from Models.News import News
from Controllers.BaseController import BaseController
class NewsController(BaseController):
    """класс прослойка - управление данными новостей для api и переопределение методов"""
    model = News
