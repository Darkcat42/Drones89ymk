from Models.Users import Users
from Controllers.BaseController import BaseController
class UsersController(BaseController):
    """класс прослойка - управление данными пользователей для api и переопределение методов"""
    model = Users
    





