from disable.Sections import Sections
from Controllers.BaseController import BaseController
class SectionsController(BaseController):
    """класс прослойка - управление данными секций для api и переопределение методов"""
    model = Sections
