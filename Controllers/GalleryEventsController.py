from Models.GalleryEvents import GalleryEvents
from Controllers.BaseController import BaseController
class GalleryEventsController(BaseController):
    model = GalleryEvents
    """управление галереями"""
    @classmethod
    def showLast(cls):
        return GalleryEvents.select().order_by(GalleryEvents.id.desc()).get()





