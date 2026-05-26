from Models.Images import Images
import os, pathlib, shutil
from Controllers.converterWeb import ConverterWeb
from Controllers.BaseController import BaseController
from flask_admin.form import ImageUploadField
from flask_admin.form.upload import ImageUploadField
from wtforms import MultipleFileField
from werkzeug.utils import secure_filename
from wtforms.widgets import FileInput
from markupsafe import Markup
from werkzeug.datastructures import FileStorage
from Models.images_models import Images_models
class ImagesController(ConverterWeb, BaseController, ImageUploadField):
    """класс прослойка - управление данными картинок для api и переопределение методов"""
    model = Images
    def _save_file(self, data, filename):
        # filename название отправленного файла а не формы
        new_filename = pathlib.Path(filename).stem + '.webp'
        root_dir = pathlib.Path(__file__).resolve().parents[1]
        image = ConverterWeb.convertDataImage(data=data)
        image.save(os.path.join(root_dir, 'static', 'webp', new_filename))
        return new_filename
    @classmethod
    def delete_image_with_file(cls, image_id):
        if cls.model is None:
            return []
        try:
            img = cls.show_id(image_id)
            cls.delete(img.id)
            os.remove(f'static/{img.src}') 
        except:
            return False
class MultipleFileInput(FileInput):
    """Виджет для <input type="file" multiple>""" 
    def __call__(self, field, **kwargs):
        kwargs.setdefault('multiple', True)
        return super().__call__(field, **kwargs)
class Images_modelsController(BaseController):
    model = Images_models
    @classmethod
    def get_where_row_id(cls, row_id):
        if cls.model is None:
            return []
        try:
            return cls.model.select().where(cls.model.row_id == row_id).execute()   
        except:
            return False
    @classmethod
    def get_where_modelName(cls, modelName):
        if cls.model is None:
            return []
        try:
            return cls.model.select().where(cls.model.model_name == modelName).execute()   
        except:
            return False
    @classmethod
    def delete_by_images_id(cls, image_id):
        if cls.model is None:
            return []
        try:
            cls.model.delete().where(cls.model.images_id == image_id).execute()
            ImagesController.delete_image_with_file(image_id)
            return True
        except:
            return False
    
    



