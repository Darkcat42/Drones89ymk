from Models.old.Paragraphs import *
class ParagraphsController():
    """ описаны методы управления данными в таблице роли"""
    """класс для модели с текстами, хранит текста из блоков"""
    @classmethod
    def get(cls):
        """геттер всей таблицы"""
        return Paragraphs.select()
    @classmethod
    def get_by_id(cls, search_id):
        """геттер по id (get or none) """
        return Paragraphs.get_or_none(Paragraphs.id==search_id)
if __name__ == '__main__':
    pass