from Models.Mainblock import Mainblock 

class MainblockController():
    # @ classmethod
    # def add_link(cls):
    #     pass
    @ classmethod
    def get_blocks_where_webpage(cls, webpage_id):
        # try:
            select = Mainblock.select().where(Mainblock.webpage_id == webpage_id) 
            return select.order_by(Mainblock.position, 'asc')
    @ classmethod
    def get_blocks_order_by_pos(cls, select):
            return select.order_by(Mainblock.position, 'asc')
    @classmethod
    def get_by_id(cls, id):
        return Mainblock.get_or_none(Mainblock.id == id)
     
    @classmethod
    def get_order_by_mainblocks(cls, select):
        list_mainblocks = cls.get_blocks_order_by_pos(select)
        mainblocks_content = []
        for mainblocks_obj in list_mainblocks:
            mainblock = []
            mainblock.append(mainblocks_obj.html_id)
            mainblock.append(mainblocks_obj.title_id)
            mainblock.append(mainblocks_obj.paragraph_id)
            mainblock.append(mainblocks_obj.media_id)
            mainblock.append(mainblocks_obj.position)
            # mainblock.append(mainblocks_obj.id)
            mainblocks_content.append(mainblock)
        return mainblocks_content
        # except:
            # return False
    # @ classmethod
    # def add_link(cls, name, url, type_link, position):
    #     return Webpage.create(
    #         name=name,
    #         url=url,
    #         type=type_link,
    #         position=position
    #     )
    #     # delete удаление записи
    # @classmethod
    # def delete(cls, id):
    #     Webpage.delete().where(Webpage.id == id).execute()
    # @classmethod
    # def get_by_url(cls, url):
    #     return Webpage.get_or_none(Webpage.url == url) 
    # @classmethod
    # def get_order_by_webpages(cls):
    #     list_webpages = cls.get_links_order_by_pos()
    #     webpage_links = []
    #     for webpage_obj in list_webpages:
    #         link = []
    #         link.append(webpage_obj.name)
    #         link.append(webpage_obj.url)
    #         link.append(webpage_obj.id)
    #         webpage_links.append(link)
    #     return webpage_links

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


