from Models.Persons_types import *
class Persons_typesController():
    """управление типом персон (как роли пользователей но тут юр физ коллектив и тп)"""
    @classmethod
    def get(cls):
        return Persons_types.select()
    @classmethod
    def add(cls):
        Persons_types.create(
            
        )
    @classmethod
    def delete(cls, id):
        return Persons_types.delete().where(Persons_types.id == id).execute()
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Persons_types.update({key:value}).where(Persons_types.id == id).execute()
    # @classmethod
    # def getNews(cls, getter_result):
    #     news = getter_result
    #     news_list = []
    #     for new in news:
    #         new_dict = {}
    #         new_dict['id'] = new.id
    #         new_dict['title'] = new.title
    #         new_dict['news_desc'] = new.news_desc
    #         new_dict['date'] = new.date
    #         new_dict['image_src'] = new.image_id.src
    #         news_list.append(new_dict)
    #     return news_list
    
    # @classmethod
    # def getNew_dict(cls, id):
    #     new = NewsController.show(id)
    #     new_dict = {}
    #     new_dict['id'] = new.id
    #     new_dict['title'] = new.title
    #     new_dict['news_desc'] = new.news_desc
    #     new_dict['date'] = new.date
    #     new_dict['image_src'] = new.image_id.src
    #     return new_dict
    # @classmethod
    # def show(cls, id):
    #     return News.get_or_none(News.id == id)
    # @classmethod
    # def getLast_dict(cls):
    #     new = News.select().order_by(News.id.desc())
    #     new_dict = {}
    #     try:
    #         new_dict['id'] = new[0].id
    #         new_dict['title'] = new[0].title
    #         new_dict['news_desc'] = new[0].news_desc
    #         new_dict['date'] = new[0].date
    #         new_dict['image_src'] = new[0].image_id.src
    #     except IndexError:
    #         new_dict['id'] = 1
    #         new_dict['title'] = 'Новостей пока нет'
    #         new_dict['news_desc'] = 'Здесь будет текст будущих вестей'
    #         new_dict['date'] = datetime.datetime.date(datetime.datetime.now())
    #         new_dict['image_src'] = 'место под изображение'
    #     return new_dict