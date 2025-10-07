from Models.Mainblock import Mainblock 
class MainblockController():
    @ classmethod
    def get_blocks_where_webpage(cls, webpage_id):
        """
        метод загрузки блоков с элементами по id веб-страниц (Webpage)
        на вход id веб-страницы
        return: объект из бд сортированный по возрастанию по position
        """
        select = Mainblock.select().where(Mainblock.webpage_id == webpage_id) 
        return select.order_by(Mainblock.position, 'asc')
    @ classmethod
    def get_blocks_order_by_pos(cls, select):
        """
        метод сортировки блоков с элементами по позиции 
        на вход объект из бд с блоками
        return: объект из бд сортированный по возрастанию по position
        """
        return select.order_by(Mainblock.position, 'asc')
    @classmethod
    def get_by_id(cls, id):
        """
        метод вывода по id 
        return: блок с элементами по id 
        """
        return Mainblock.get_or_none(Mainblock.id == id)
    @classmethod
    def get_order_by_mainblocks(cls, select):
        """
        метод перебора блоков с элементами для передачи  
        массива с данными в шаблонизатор html
        return: массив с объектами в форме массивов
        """
        list_mainblocks = cls.get_blocks_order_by_pos(select)
        mainblocks_content = []
        for mainblocks_obj in list_mainblocks:
            mainblock = []
            mainblock.append(mainblocks_obj.html_id)
            mainblock.append(mainblocks_obj.title_id)
            mainblock.append(mainblocks_obj.paragraph_id)
            mainblock.append(mainblocks_obj.media_id)
            mainblock.append(mainblocks_obj.position)
            mainblocks_content.append(mainblock)
        return mainblocks_content
if __name__ == '__main__':
    pass


