from Models.GalleryEvents import *
class GalleryEventsController():
    """
        управление данными таблицы 
    """
    @classmethod
    def get(cls):
        return GalleryEvents.select()
    @classmethod
    def add(cls, date, title):
        return GalleryEvents.create(
            date=date,
            title=title
        )
    @classmethod
    def getGalleryEvents(cls):
        pass
        # news = cls.get()
        # news_list = []
        # for new in news:
        #     new_dict = {}
        #     new_dict['id'] = new.id
        #     new_dict['title'] = new.title
        #     new_dict['news_desc'] = new.news_desc
        #     new_dict['date'] = new.date
        #     new_dict['image_src'] = new.image_id.src
        #     news_list.append(new_dict)
        # return news_list
    @classmethod
    def showLast(cls):
        return GalleryEvents.select().order_by(GalleryEvents.id.desc()).get()
if __name__ == '__main__':
    pass




