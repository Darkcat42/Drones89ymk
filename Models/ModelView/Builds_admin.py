from Models.Builds_authors import Builds_authors

from Models.Builds_hardwares import Builds_hardwares
from flask_admin.contrib.peewee import ModelView

from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Builds_admin(ModelView):
    # переопределяем страницу
    list_template = 'admin/custom/builds/list.html'
    edit_template = 'admin/custom/builds/edit.html'
    create_template = 'admin/custom/builds/create.html'
    # указываем какие модели необходимо дополнитель добавить при создании записи сборок

    inline_models = (
        (Builds_authors),
        (Builds_hardwares )
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
    def _builds_authors_formatter(view, context, model, name):
        persons_names = []
        for relation in model.builds:
            persons_names.append(relation.persons_id.firstName)
        return Markup(f'<p>f{persons_names}</p>')
    
    # форматируем сами столбцы
    column_labels = {
        'build_name' : 'название сборки',
        'inch' : 'размер дюймах',
        'hardwares': 'Оборудование',
        # 'persons': 'Автор',
        'build_desc' : 'описание сборки',
        'build_image_id' : 'изображение сборки',

    }
    form_args = {
        'build_name' : {'label' : 'Название сборки'} , 
        'inch' : {'label' : 'Размер дюймах'} ,
        'hardwares': {'label' : Markup('<a href=''>Оборудование</a>')} ,
        # 'persons': 'Автор',
        'build_desc' : {'label' : 'Описание сборки'} ,
        'build_image_id' : {'label' : 'Изображение сборки'} ,

    }
    # настройка порядка столбоцев (почему то не работает)
    column_list = {
        'build_name',
        'inch',
        'build_desc',
        'hardwares',
        # 'persons',
        'build_image_id',

    }
    # форматируем значения в столбцах
    column_formatters = {
        'build_image_id': _build_image_id_img_formatter,
        'hardwares': _build_hardwares_formatter,
        # 'persons': _builds_authors_formatter,
    }
    