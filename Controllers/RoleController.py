# класс в котором описаны методы управления данными в таблице роли
from Models.Roles import *

class RoleController():
    # метод create для новых записей
    @classmethod
    def add(cls, name):
        Roles.create(name=name)
    # метод read для вывода записей
    @classmethod
    def get(cls):
        return Roles.select().order_by(Roles.name)
    # @classmethod
    # def get_by_id(cls, id):
    #     return Roles.select().where(Roles.id == id).id
    # вывод одной записи по id
    @classmethod
    def show(cls, id):
        # return Roles.select().where(Roles.id == id) # вывод и фильтруют информацию
        # return  Roles.get(id)
        # return Roles.get_or_none(id)
        return Roles.get_by_id(id)
    #вывод записи по имени
    @classmethod
    def show_name(cls, name):
        return Roles.get_or_none(Roles.name == name)
    # обновление записи
    @classmethod
    def update(cls, id, new_name):
        Roles.update({Roles.name: new_name}).where(Roles.id == id).execute()

    @classmethod
    def update_all(cls, id, new_id, new_name):
        Roles.update({Roles.id:new_id, Roles.name: new_name}).where(Roles.id == id).execute()

    # delete удаление записи
    @classmethod
    def delete(cls, id):
        Roles.delete().where(Roles.id == id).execute()


if __name__ == '__main__':
  #  RoleController.add('Manager')
  #   print(RoleController.get())
    for role in RoleController.get():
        print((role.id, role.name))
    # print(RoleController.show(1).name)
    # RoleController.update(1, 'Администратор')
    # print(RoleController.show_name('Администратор').name)
    # RoleController.delete(3)
    # RoleController.delete(2)

