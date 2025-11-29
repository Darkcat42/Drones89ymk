from Models.Images import *
from Controllers.converterWeb import ConverterWeb
class ImagesController(ConverterWeb):
    """
        управление картинками
    """
    @classmethod
    def get(cls):
        return Images.select()
    @classmethod
    def add(cls, filename, src, alt='' ):
        return Images.create(
            filename=filename,
            src=src,
            alt=alt
        )
    @classmethod
    def show(cls, filename):
        return Images.get_or_none(Images.filename == filename)
    @classmethod
    def show_id(cls, id):
        return Images.get_or_none(Images.id == id)
if __name__ == '__main__':
   pass