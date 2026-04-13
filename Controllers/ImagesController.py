from Models.Images import Images
import os, pathlib
from Controllers.converterWeb import ConverterWeb
from Controllers.BaseController import BaseController
from flask_admin.form import ImageUploadField
class ImagesController(ConverterWeb, BaseController, ImageUploadField):
    """класс прослойка - управление данными картинок для api и переопределение методов"""
    model = Images
    def _save_file(self, data, filename):
        new_filename = pathlib.Path(filename).stem + '.webp'
        root_dir = pathlib.Path(__file__).resolve().parents[1]
        image = ConverterWeb.convertDataImage(data=data)
        image.save(os.path.join(root_dir, 'static', 'webp', new_filename))
        return new_filename


