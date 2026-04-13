from Models.Statistics import Statistics
from Controllers.BaseController import BaseController
class StatisticsController(BaseController):
    """класс прослойка - управление данными расписания для api и переопределение методов"""
    model = Statistics
    



