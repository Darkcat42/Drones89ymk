from Models.GalleryEvents import *
class GalleryEventsController():
    """управление галереями"""
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
    def delete(cls, id):
        return GalleryEvents.delete().where(GalleryEvents.id == id).execute()
    @classmethod
    def update(cls, id, **kwargs):
        GalleryEvents.update(**kwargs).where(GalleryEvents.id == id).execute()
    # @classmethod
    # def update(cls, id, **filds):
    #     for key, value in filds.items():
    #         GalleryEvents.update({key:value}).where(GalleryEvents.id == id).execute()
    @classmethod
    def show(cls, id):
        return GalleryEvents.get_or_none(GalleryEvents.id == id)
    @classmethod
    def showLast(cls):
        return GalleryEvents.select().order_by(GalleryEvents.id.desc()).get()
if __name__ == '__main__':
    pass




