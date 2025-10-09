from Models.Roles import *
class RoleController():
    """класс в котором описаны методы управления данными в таблице роли"""
    @classmethod
    def add(cls, name):
        """метод create для записи новых ролей
        принимает строку с новой ролью"""
        Roles.create(name=name)
    @classmethod
    def get(cls):
        """метод read для вывода записей (order_by(name))"""
        return Roles.select().order_by(Roles.name)
    @classmethod
    def show(cls, id):
        """метод show вывод роли по id"""
        return Roles.get_by_id(id)
    @classmethod
    def show_name(cls, name):
        """метод show_name вывод записи по роли"""
        return Roles.get_or_none(Roles.name == name)
    @classmethod
    def update(cls, id, new_name):
        """метод update модели Roles для обновления записи о роли
        принимает id и строку с новой ролью"""
        Roles.update({Roles.name: new_name}).where(Roles.id == id).execute()
    @classmethod
    def delete(cls, id):
        """метод delete для удаления записи"""
        Roles.delete().where(Roles.id == id).execute()



