from Models.Builds_authors import Builds_authors
from Models.Builds_hardwares import Builds_hardwares
from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Builds_admin(ModelView):
    
    # переопределяем страницу
    list_template = 'admin/templates_admin/builds/list.html'
    edit_template = 'admin/custom/builds/edit.html'
    create_template = 'admin/custom/builds/create.html'
    # указываем какие модели необходимо дополнитель добавить при создании записи сборок
    inline_models = (
        (Builds_authors, {
            'label' : 'авторы'
        }),
        (Builds_hardwares, {
            'label' : 'оборудование'
        } )
        )
    # загружаем в объект представления flask-admin данные для меню панели администраора
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Сборки'
        super().__init__(model, *args, **kwargs)
    def _build_image_id_img_formatter(view, context, model, name):
        build_image_src = model.build_image_id.src
        if not build_image_src:
            return ""
        if not build_image_src: 
            return ""
        return Markup(f'<img src="../../{build_image_src}" class="img-fluid" alt="...">')
    def _build_hardwares_formatter(view, context, model, name):
        hardwares_names = []
        for relation in model.hardwares:
            hardwares_names.append(relation.Hardwares_id.category)

        return Markup(f'<p>f{hardwares_names}</p>')
    
    
    # форматируем сами столбцы
    column_labels = {
        'build_name' : 'название сборки',
        'inch' : 'размер дюймах',
        'hardwares': Markup('<a href=''>оборудование</a>'),
        'build_desc' : 'описание сборки',
        'build_image_id' : 'изображение сборки',
        
    }
    column_list = {
        'build_name',
        'inch',
        'build_desc',
        'hardwares',
        'build_image_id',
        
    }
    # форматируем значения в столбцах
    column_formatters = {
        'build_image_id': _build_image_id_img_formatter,
        'hardwares': _build_hardwares_formatter
    }
    