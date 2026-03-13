from Models.GalleryEvents import GalleryEvents
from Controllers.ModelsController import ModelsController
class GalleryEventsController(ModelsController):
    model = GalleryEvents
    """управление галереями"""
    @classmethod
    def showLast(cls):
        return GalleryEvents.select().order_by(GalleryEvents.id.desc()).get()





