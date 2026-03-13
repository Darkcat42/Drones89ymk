from Models.Roles import Roles
from Controllers.ModelsController import ModelsController
class RoleController(ModelsController):
    """класс в котором описаны методы управления данными в таблице роли"""
    model = Roles
    @classmethod
    def show_name(cls, name):
        """метод show_name вывод записи по роли"""
        return Roles.get_or_none(Roles.name == name)




