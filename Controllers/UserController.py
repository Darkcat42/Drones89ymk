from Models.Users import Users
from Controllers.ModelsController import ModelsController
class UsersController(ModelsController):
    model = Users
    """управление пользователями"""
    @classmethod
    def get_by_login(cls, search_login):
        return Users.get_or_none(Users.login == search_login)






