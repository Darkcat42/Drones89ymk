from Models.Paragraphs import *
class ParagraphsController():

    @classmethod
    def get(cls):
        return Paragraphs.select()


    @classmethod
    def get_by_login(cls, search_id):
        return Paragraphs.get_or_none(Paragraphs.id==search_id)


if __name__ == '__main__':
    pass