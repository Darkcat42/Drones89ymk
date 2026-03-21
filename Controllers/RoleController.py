from Models.Roles import Roles
from Controllers.BaseController import BaseController
class RoleController(BaseController):
    """класс прослойка - управление данными ролей для api и переопределение методов"""
    model = Roles
    # @classmethod
    # def show_name(cls, name):
    #     """метод show_name вывод записи по роли"""
    #     return Roles.get_or_none(Roles.name == name)




