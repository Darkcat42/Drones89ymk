from Models.GalleryEvents import *
from Models.Images import *
from Models.GalleryEvents_images import *
from Controllers.ImagesController import ImagesController
from Controllers.GalleryEventsController import GalleryEventsController
class GalleryEvents_imagesController():
    """управление наборами картинок для конкретной галереи (каждой галереи)"""
    @classmethod
    def get(cls):
        return GalleryEvents_images.select()
    @classmethod
    def show_gallery_images(cls, id):
        return GalleryEvents_images.get_or_none(GalleryEvents_images.galleryEvent_id == id)
    @classmethod
    def delete(cls, id):
        return GalleryEvents_images.delete().where(GalleryEvents_images.galleryEvent_id == id).execute()
    @classmethod
    def add(cls, **kwargs):
        return GalleryEvents_images.create(**kwargs)
    @classmethod
    def update(cls, id, **kwargs):
        GalleryEvents_images.update(**kwargs).where(GalleryEvents_images.id == id).execute()
    # @classmethod
    # def update(cls, id, **kwargs):
    #     for key, value in kwargs.items():
    #         GalleryEvents_images.update({key:value}).where(GalleryEvents_images.id == id).execute()
    @classmethod
    def get_cur_gallery(cls, id):
        galleryEvents = GalleryEventsController.show(id)
        galleryEvents_images = GalleryEvents_images.select().where(GalleryEvents_images.galleryEvent_id == galleryEvents.id)
        list_of_images = []
        for gallery_image in galleryEvents_images:
            image = ImagesController.show_id(gallery_image.image_id)
            list_of_images.append([image.id, image.src])
        current_gallery = {}
        current_gallery['id'] = galleryEvents.id
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
                list_of_images.append([image.id, image.src])
            current_gallery = {}
            current_gallery['id'] = gallery.id
            current_gallery['title'] = gallery.title
            current_gallery['date'] = gallery.date
            current_gallery['images'] = list_of_images
            list_of_gallerys.append(current_gallery)
        return list_of_gallerys




