from Models.GalleryEvents import *
from Models.Images import *
from Models.GalleryEvents_images import *
from Controllers.ImagesController import ImagesController
from Controllers.GalleryEventsController import GalleryEventsController
class GalleryEvents_imagesController():
    """
        управление данными таблицы расписание
    """
    @classmethod
    def get(cls):
        return GalleryEvents_images.select()
    @classmethod
    def add(cls, image_id, galleryEvent_id):
        return GalleryEvents_images.create(
            image_id=image_id,
            galleryEvent_id=galleryEvent_id
        )
    @classmethod
    def get_cur_gallery(cls, galleryEvents):
        galleryEvents_images = GalleryEvents_images.select().where(GalleryEvents_images.galleryEvent_id == galleryEvents.id)
        list_of_images = []
        for gallery_image in galleryEvents_images:
            list_of_images.append(gallery_image.image_id)
        current_gallery = {}
        current_gallery['title'] = galleryEvents.title
        current_gallery['date'] = galleryEvents.date
        current_gallery['images'] = list_of_images
        return current_gallery
    @classmethod
    def get_all_gallerys(cls):
        list_of_gallerys = []
        select_obj = GalleryEventsController.get()
        for gallery in select_obj:
            galleryEvents_images = GalleryEvents_images.select().where(GalleryEvents_images.galleryEvent_id == gallery.id)
            list_of_images = []
            for gallery_image in galleryEvents_images:
                image = ImagesController.show_id(gallery_image.image_id)
                list_of_images.append(image.src)
            current_gallery = {}
            current_gallery['title'] = gallery.title
            current_gallery['date'] = gallery.date
            current_gallery['images'] = list_of_images
            list_of_gallerys.append(current_gallery)
        return list_of_gallerys
if __name__ == '__main__':
    pass




