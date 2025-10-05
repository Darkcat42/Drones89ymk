# класс в котором описаны методы управления данными в таблице роли
from Models.Webpage import Webpage 

class WebpageController():
    @ classmethod
    def add_link(cls):
        pass
    @ classmethod
    def get_links_order_by_pos(cls):
        return Webpage.select().order_by(Webpage.position, 'asc')
    @ classmethod
    def add_link(cls, name, url, type_link, position):
        return Webpage.create(
            name=name,
            url=url,
            type=type_link,
            position=position
        )
        # delete удаление записи
    @classmethod
    def delete(cls, id):
        Webpage.delete().where(Webpage.id == id).execute()
    @classmethod
    def get_by_url(cls, url):
        return Webpage.get_or_none(Webpage.url == url) 
    @classmethod
    def get_order_by_webpages(cls):
        list_webpages = cls.get_links_order_by_pos()
        webpage_links = []
        for webpage_obj in list_webpages:
            link = []
            link.append(webpage_obj.name)
            link.append(webpage_obj.url)
            link.append(webpage_obj.id)
            webpage_links.append(link)
        return webpage_links

    # # метод create для новых записей
    # @classmethod
    # def add(cls, name):
    #     Roles.create(name=name)
    # # метод read для вывода записей
    # @classmethod
    # def get(cls):
    #     return Roles.select().order_by(Roles.name)
    # # @classmethod
    # # def get_by_id(cls, id):
    # #     return Roles.select().where(Roles.id == id).id
    # # вывод одной записи по id
    # @classmethod
    # def show(cls, id):
    #     # return Roles.select().where(Roles.id == id) # вывод и фильтруют информацию
    #     # return  Roles.get(id)
    #     # return Roles.get_or_none(id)
    #     return Roles.get_by_id(id)
    # #вывод записи по имени
    # @classmethod
    # def show_name(cls, name):
    #     return Roles.get_or_none(Roles.name == name)
    # # обновление записи
    # @classmethod
    # def update(cls, id, new_name):
    #     Roles.update({Roles.name: new_name}).where(Roles.id == id).execute()

    # @classmethod
    # def update_all(cls, id, new_id, new_name):
    #     Roles.update({Roles.id:new_id, Roles.name: new_name}).where(Roles.id == id).execute()




# if __name__ == '__main__':
#     pass
    # for role in RoleController.get():
    #     print((role.id, role.name))


