from Models.Persons_types import Persons_types
from Controllers.BaseController import BaseController
class Persons_typesController(BaseController):
    """класс прослойка - управление данными о типах персон для api и переопределение методов"""
    model = Persons_types
    