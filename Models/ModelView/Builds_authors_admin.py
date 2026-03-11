from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Builds_authors_admin(ModelView):
    # загружаем в объект представления flask-admin данные для меню панели администраора
    def __init__(self, model, *args, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = 'Сборки и Авторы'
        super().__init__(model, *args, **kwargs)
    def _persons_link_formatter(view, context, model, name):
        person = model.persons_id
        if not person:
            return ""
        full_name = f"{person.firstName} {person.lastName}"
        url = url_for('persons.index_view') # есть также edit_view delete_view и тп
        return Markup(f'<a href="{url}">{full_name}</a>')
    def _builds_link_formatter(view, context, model, name):
        build = model.builds_id
        if not build:
            return ""
        build_name = str(build.build_name) 
        url = url_for('builds.index_view') # есть также edit_view delete_view и тп
        if not build_name:
            return Markup(f'<a href="{url}">К сборкам</a>')
        return Markup(f'<a href="{url}">{build_name}</a>')
    # форматируем значения в столбцах
    column_formatters = {
        'persons_id': _persons_link_formatter,
        'builds_id' : _builds_link_formatter
    }
    # форматируем сами столбцы
    column_labels = {
        'persons_id' : 'персоны',
        'builds_id' : 'сборки'
    }