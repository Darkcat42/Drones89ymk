from Models.News import *
import datetime
class NewsController():
    """
        управление данными таблицы расписание
    """
    @classmethod
    def get(cls):
        return News.select()
    @classmethod
    def getDesc(cls):
        return News.select(News.id.desc())
    @classmethod
    def addNews(cls, title, news_desc, date, image_id):
        News.create(
            title=title,
            news_desc=news_desc,
            date=date,
            image_id=image_id
        )
    @classmethod
    def getNews(cls, getter_result):
        news = getter_result
        news_list = []
        for new in news:
            new_dict = {}
            new_dict['id'] = new.id
            new_dict['title'] = new.title
            new_dict['news_desc'] = new.news_desc
            new_dict['date'] = new.date
            new_dict['image_src'] = new.image_id.src
            news_list.append(new_dict)
        return news_list
    @classmethod
    def getNew_dict(cls, id):
        new = cls.show(id)
        new_dict = {}
        new_dict['id'] = new.id
        new_dict['title'] = new.title
        new_dict['news_desc'] = new.news_desc
        new_dict['date'] = new.date
        new_dict['image_src'] = new.image_id.src
        return new_dict
    @classmethod
    def show(cls, id):
        return News.select().get_or_none(id)
    @classmethod
    def getLast_dict(cls):
        new = News.select().order_by(News.id.desc())
        new_dict = {}
        try:
            new_dict['id'] = new[0].id
            new_dict['title'] = new[0].title
            new_dict['news_desc'] = new[0].news_desc
            new_dict['date'] = new[0].date
            new_dict['image_src'] = new[0].image_id.src
        except IndexError:
            new_dict['id'] = 1
            new_dict['title'] = 'Новостей пока нет'
            new_dict['news_desc'] = 'Здесь будет текст будущих вестей'
            new_dict['date'] = datetime.datetime.date(datetime.datetime.now())
            new_dict['image_src'] = 'место под изображение'
        return new_dict




