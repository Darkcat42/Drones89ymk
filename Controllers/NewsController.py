from Models.News import *
class NewsController():
    """
        управление данными таблицы расписание
    """
    @classmethod
    def get(cls):
        return News.select()
    @classmethod
    def getDesc(cls):
        return News.select()
    @classmethod
    def addNews(cls, title, news_desc, date, image_id):
        News.create(
            title=title,
            news_desc=news_desc,
            date=date,
            image_id=image_id
        )
    
    @classmethod
    def getNews(cls):
        news = cls.get()
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
    def showLast(cls):
        return News.select().order_by(News.id.desc()).get()
    @classmethod
    def getLast_dict(cls):
        new = News.select().order_by(News.id.desc()).get()
        new_dict = {}
        new_dict['id'] = new.id
        new_dict['title'] = new.title
        new_dict['news_desc'] = new.news_desc
        new_dict['date'] = new.date
        new_dict['image_src'] = new.image_id.src
        return new_dict




