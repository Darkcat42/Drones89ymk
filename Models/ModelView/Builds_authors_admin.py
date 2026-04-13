# импорты
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
from Models.ModelView.BaseModelView import BaseModelView
class Builds_authors_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Сборки и авторы'
    uses_upload = False
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)

    def _persons_link_formatter(view, context, model, name):
        person = model.persons_id
        full_name = f"{person.firstName} {person.lastName}"
        url = url_for('persons.index_view') # есть также edit_view delete_view и тп
        return Markup(f'<a href="{url}">{full_name}</a>')
    def _builds_link_formatter(view, context, model, name):
        build = model.builds_id
        build_name = str(build.build_name) 
        url = url_for('builds.index_view') # есть также edit_view delete_view и тп
        if not build_name:
            return Markup(f'<a href="{url}">К сборкам</a>')
        return Markup(f'<a href="{url}">{build_name}</a>')
    # форматируем сами столбцы
    column_labels = {
        'persons_id' : 'персоны', 
        'builds_id' : 'сборки'}
    # форматируем значения в таблице, если нет то None для логики генератора словаря
    formatter_list = [
        _persons_link_formatter,
        _builds_link_formatter]
   