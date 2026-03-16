from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from Controllers.ImagesController import ImagesController
from flask import url_for
from flask import current_app
from pathlib import Path
import os
from wtforms import FileField
class Images_admin(ModelView):
    def on_model_change(self, form, model, is_created):
        filename = form.filename.data
        file = form.src.data
        alt = form.alt.data


        filename = form.filename.data
        dir_name = current_app.appСontorller.make_categoryDir('news')
        if Path(filename).suffix != '.webp':
            fileSrc = os.path.join(current_app.appСontorller.tempImg, filename)
            current_app.appСontorller.make_recurDirs(current_app.appСontorller.tempImg)
            file.save(fileSrc) # сохраняем файл во временную папку
            webp_src = ImagesController.convertImage(fileSrc, dir_name)

            filename = str(Path(filename).stem)+'.webp'
        else:
            webp_src = os.path.join(dir_name, filename)
            file.save(webp_src)
        # image = ImagesController.add(
        #     filename=filename,
        #     src=webp_src,
        #     alt=alt)
        model.filename = filename
        model.src = webp_src
        model.alt = alt
        return super().on_model_change(form, model, is_created)



        # ImagesController.add(
        #     filename = filename,
        #     src = file_data,
        #     alt = alt
        #  )
    #      id = PrimaryKeyField()
    # filename = CharField()
    # src = TextField()
    # alt = TextField()
         
    edit_template = 'admin/custom/images/edit.html'
    create_template = 'admin/custom/images/create.html'
    page_size = 20
    # Переопределяем поле модели на поле файла для формы
    form_overrides = {
         'src' : FileField
    }

    can_set_page_size = True
    def __init__(self, model, *args, **kwargs):
            if 'name' not in kwargs:
                kwargs['name'] = 'Картинки'
            super().__init__(model, *args, **kwargs)
    def _image_formatter(view, context, model, name):
        image_src = model.src
        if not image_src:
            return ""
        image_src = image_src.replace('static\\', '')
        image_src = image_src.replace('\\', '/')
        src = url_for('static', filename=image_src)
        # return Markup(f'<img data-src="../../{image_src}" class="img-fluid fsi lazy" alt="...">')
        return Markup(f'<img src="{src}" class="w-100 lazy" loading="lazy" alt="..."> ')
    # форматируем сами столбцы
    column_labels = {
        'filename' : 'файл',
        'src' : 'путь до файла',
        'alt' : 'подпись картинки',
        'prev' : Markup('<a href=''>картинка</a>'),
    }
    column_formatters = {
        'prev': _image_formatter,
    }
    column_list = {
        'filename',
        'prev',
        'src',
        'alt',
        
    }
    column_searchable_list = [
        'filename',
        'src',
        'alt',]
#     """
#     модель таблицы изображения
#     """
#     id = PrimaryKeyField()
#     filename = CharField()
#     src = TextField()
#     alt = TextField()
# if __name__ == '__main__':
#     connect_db().create_tables([Images])
    