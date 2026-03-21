from Models.Images import Images
from Controllers.converterWeb import ConverterWeb
from Controllers.BaseController import BaseController
class ImagesController(ConverterWeb, BaseController):
    """класс прослойка - управление данными картинок для api и переопределение методов"""
    model = Images
    # @classmethod
    # def show(cls, filename):
    #     return Images.get_or_none(Images.filename == filename)
#     @classmethod
#     def show(cls, id):
#         return Images.get_or_none(Images.id == id)
# if __name__ == '__main__':
#    pass