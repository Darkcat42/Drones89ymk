# системные импорты
from flask_admin.contrib.peewee import ModelView
from pathlib import Path
from flask import request, url_for, flash, redirect
import os, shutil
from peewee import TextField, CharField
from flask_admin import expose
# импорты моих модулей
from Controllers.ImagesController import *

class BaseModelView(ModelView):
    """содержит единую логику для всех ModelView"""
    uses_multi_upload = False
    uses_upload = False
    image_prev = False
    # логика для подключенной БД
    column_labels = {}
    column_list = ()
    form_extra_fields = {} # ?!
    formatter_list = []
    form_args = {}
    modelTableName = ''
    can_set_page_size = True
    page_size = 20
    images_list = []
    root_dir = Path(__file__).resolve().parents[2]
    file_path = os.path.join(root_dir, 'static/webp')
    
    def __init__(self, model, modelTableName, *args, **kwargs):
        if self.uses_upload:
            self.form_extra_fields = {
            'upload': ImagesController(
                'image',
                base_path = os.path.join(Path(__file__).resolve().parents[2], 'static/webp'),  
                url_relative_path=f'webp/',         # URL ПУТЬ (для браузера, относительно /static/)
                thumbnail_size=(100, 100, True),    # Создать превью 100x100 с кропом
                allow_overwrite=True,
                allowed_extensions=['jpg', 'jpeg', 'png', 'webp']
                )
            }
        if self.uses_multi_upload:
            self.form_extra_fields = {
            'multi_upload': MultipleFileField('загрузить изображения')
            }
        if self.uses_multi_upload and self.image_prev:
            self.form_extra_fields = {
            'upload': ImagesController(
                'Превью',
                base_path = os.path.join(Path(__file__).resolve().parents[2], 'static/webp'),  
                url_relative_path=f'webp/',         # URL ПУТЬ (для браузера, относительно /static/)
                thumbnail_size=(100, 100, True),    # Создать превью 100x100 с кропом
                allow_overwrite=True,
                allowed_extensions=['jpg', 'jpeg', 'png', 'webp']
                ),
            'multi_upload': MultipleFileField('загрузить изображения')
            }
        labels_keys = self.column_labels.keys()
        labels_val = self.column_labels.values()
        # создаем множество определяющее количество столбоцов
        self.column_list = (set_item for set_item in labels_keys)
        # указываем функцию обработки данных для конкретного столбца
        self.column_formatters = dict(zip(labels_keys, self.formatter_list))
        # включаем поиск по столбцам модели
        self.column_searchable_list = [labels for labels, field in model._meta.fields.items() if isinstance(field, (CharField, TextField))] 
        # используя column_labels чиним названия полей в формах create и edit 
        self.form_args = {
            key: {'label':val}
            for key, val in zip(labels_keys, labels_val)
        }
        # ловим и устанавливаем имя модели в админ панели
        if 'name' not in kwargs:
            kwargs['name'] = modelTableName
        super().__init__(model, *args, **kwargs)
    
    @expose('/') # метод срабатывает при ошибке и дает уведомление
    def index_view(self):
        try:
            return super().index_view()
        except Exception as e:
            flash(f"ошибка: {str(e)}", 'error')
            return redirect('/admin/') # редирект на главную админки
    # логика для безопасной работы без БД
    def is_accessible(self):
        # Доступ разрешён всегда, но реальные данные отображаются только при готовой БД
        return True
    def _handle_db_unavailable(self):
        """Действие при недоступной БД (может быть переопределено)."""
        flash('База данных не подключена. Настройте подключение.', 'error')
        return redirect(url_for('add_sql'))
    @staticmethod
    # метод класса - создает категорию и перемещает туда 
    def catDirFile_save(categoryDir, curent_path, dest_path):
        if not os.path.isdir(categoryDir):
            os.mkdir(categoryDir)
        if os.path.isfile(curent_path):
            try:
                shutil.move(
                    curent_path,
                    dest_path,
                    )
            except:
                flash('ошибка shutil.move в baseModelView.on_model_change при загрузке файла в БД.', 'info')
                return False
    def delete_model(self, model):
        modelName = model.__class__.__name__
        if modelName == 'Images':
            flash('Данные удалены с диска.')
            super().delete_model(model)
    # переопределяем функцию до создания записи
    def on_model_change(self, form, model, is_created): 
        """ сюда стекаются все вызовы на загрузку картинки """
        uploaded_files = request.files.getlist('multi_upload')
        image_prev = form.upload.data if hasattr(form, 'upload') else None
        # 1. Получаем имя файла (контроллер уже сохранил его на диск)
        modelName = model.__class__.__name__
        webpDir = 'webp'
        staticDir = 'static'
        # images_list = []
        # Если файл загружен
        for file_storage in uploaded_files:
            if not file_storage or not file_storage.filename:
                continue
            # из объекта формы получаем наш переписаный в ImagesController метод
            form.upload._save_file(file_storage, file_storage.filename)  
            filenameFile = file_storage.filename # имя что вернул метод _save_file
            curent_path = os.path.join(staticDir, webpDir, str(filenameFile))
            if modelName == 'Images':
                filenameForm = f'{str(form.src.data)}.webp'  # имя что вложено в форму
                altForm = form.alt.data
                category = form.category.data 
                categoryDir = os.path.join(staticDir, webpDir, str(category))
                dest_path = os.path.join(categoryDir, str(filenameForm))
                self.catDirFile_save(categoryDir, curent_path, dest_path)
                # обновляем бд
                model.src = f'{webpDir}/{category}/{filenameForm}'
                return True
            else:
                filenameForm = f'{str(Path(filenameFile).stem)}.webp'
                altForm = '...'
                category = modelName.replace('Form', '')
                categoryDir = os.path.join(staticDir, webpDir, str(category))
                dest_path = os.path.join(categoryDir, str(filenameForm))
                self.catDirFile_save(categoryDir, curent_path, dest_path)
            # обновляем бд
            img = Images.create(
                src = f'{webpDir}/{category}/{filenameForm}',
                alt = altForm,
                category = category
            )
            self.images_list.append(img.id)
        if not image_prev:
            model.image_id = self.images_list[0]
            self.images_list.pop(0)
        else:
            filenameForm = f'{str(Path(image_prev.filename).stem)}.webp'
            curent_path = os.path.join(staticDir, webpDir, str(image_prev.filename))
            altForm = '...'
            category = modelName.replace('Form', '')
            categoryDir = os.path.join(staticDir, webpDir, str(category))
            dest_path = os.path.join(categoryDir, str(filenameForm))
            self.catDirFile_save(categoryDir, curent_path, dest_path)
            # обновляем бд
            img = Images.create(
                src = f'{webpDir}/{category}/{filenameForm}',
                alt = altForm,
                category = category
                )
            model.image_id = img.id
    # переопределяем функцию для работы непосредственно с созданной записью
    def after_model_change(self, form, model, is_created):  
        modelName = model.__class__.__name__ 
        if self.images_list:
            # обновляем бд
            for img in self.images_list:
                Images_modelsController.add(
                    model_name = modelName,
                    images_id = img,
                    row_id = model.id
                )
        self.images_list = []
    def on_model_delete(self, model):
        modelName = model.__class__.__name__
        selectImage_model = Images_modelsController.get_where_row_id(model.id)
        for image_model in selectImage_model:
            Images_modelsController.delete_by_images_id(image_model.images_id)
        

        

            
            



                
                
                   
                    

                    
    