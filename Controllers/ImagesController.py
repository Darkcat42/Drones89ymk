from Models.Images import Images
from Controllers.converterWeb import ConverterWeb
from Controllers.ModelsController import ModelsController
class ImagesController(ConverterWeb, ModelsController):
    model = Images
    """управление картинками"""
    @classmethod
    def show(cls, filename):
        return Images.get_or_none(Images.filename == filename)
    @classmethod
    def show_id(cls, id):
        return Images.get_or_none(Images.id == id)
if __name__ == '__main__':
   pass