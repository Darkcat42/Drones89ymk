from flask_admin.contrib.peewee import ModelView
from pathlib import Path
import os
from wtforms import validators
from flask import url_for, flash, redirect
from peewee import TextField, CharField
from Controllers.ImagesController import *
class BaseModelView(ModelView):
    """содержит единую логику для всех ModelView которые переопределяют ее под свои модели"""

    # логика для подключенной БД
    column_labels = {}
    column_list = ()
    # form_extra_fields = {}
    formatter_list = []
    form_args = {}
    modelTableName = ''
    can_set_page_size = True
    page_size = 20
    root_dir = Path(__file__).resolve().parents[2]
    file_path = os.path.join(root_dir, 'static/webp')
    
    def __init__(self, model, modelTableName, *args, **kwargs):
        if self.uses_upload:
            self.form_extra_fields = {
            'upload': ImagesController(
                'Картинка',
                base_path = os.path.join(Path(__file__).resolve().parents[2], 'static/webp'),  
                url_relative_path='webp/',         # URL ПУТЬ (для браузера, относительно /static/)
                thumbnail_size=(100, 100, True),    # Создать превью 100x100 с кропом
                allow_overwrite=True,
                allowed_extensions=['jpg', 'jpeg', 'png', 'webp']
                )
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
    # # логика для безопасной работы без БД
    def is_accessible(self):
        # Доступ разрешён всегда, но реальные данные отображаются только при готовой БД
        return True
    def _handle_db_unavailable(self):
        """Действие при недоступной БД (может быть переопределено)."""
        flash('База данных не подключена. Настройте подключение.', 'error')
        return redirect(url_for('add_sql'))
    def on_model_change(self, form, model, is_created):
            # Если файл загружен
            if self.uses_upload:
                if form.upload.data:
                    # 1. Получаем имя файла (контроллер уже сохранил его на диск)
                    filename = form.upload.data.filename
                    # 2. По документации Peewee: находим или создаем запись в Images
                    image_obj, created = Images.get_or_create(src=filename)
                    # 3. Привязываем объект 
                    model.image_id = image_obj
    