from Models.Hardwares import Hardwares
from Models.Builds_authors import Builds_authors
from Models.Builds_hardwares import Builds_hardwares
from Models.ModelView.BaseModelView import BaseModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
class Builds_admin(BaseModelView):
    # название модели в списке админ панели
    modelTableName = 'Сборки'
    uses_upload = True
    def __init__(self, model, modelTableName = modelTableName, *args, **kwargs):
        super().__init__(model, modelTableName, *args, **kwargs)
        # build_name = model.build_name
        # inch = model.inch  
        # hardwares = model.hardwares 
        # authors = model.authors 
        # build_desc = model.build_desc 
        # build_image_id = model.build_image_id 

    # переопределение страниц форм
    list_template = 'admin/custom/builds/list.html'
    # edit_template = 'admin/custom/builds/edit.html'
    # create_template = 'admin/custom/builds/create.html'
    # указываем какие модели необходимо дополнительно добавить при создании записи сборок
    inline_models = ((Builds_authors), (Builds_hardwares)) 
    
    # загружаем в объект представления flask-admin данные для меню панели администраора
    def _image_formatter(view, context, model, name):
        src = ' '
        tag = Markup(f'<img src="{src}" class="img-fluid" alt="...">')
        if not model.image_src:
            tag = Markup(f'<p>Ошибка внешнего ключа</p>')
        else:
            src = model.image_src
        return tag
    # данные методы переопределяют данные в столбцах
    def _hardwares_formatter(view, context, model, name):
        return [relation.Hardwares_id.category for relation in model.hardwares]
    def _authors_formatter(view, context, model, name):
        return [relation.persons_id.firstName for relation in model.authors]
    def _default_formatter(view, context, model, name):
        src = ' '
        return Markup(f'<p>Ошибка атрибута</p>')
        
    # список форматирований, порядок функций важен относительно столбцов 
    # !!! для пустых только None т.к сбивается логака фласк-админ 
    formatter_list = [
        None, 
        None,
        _hardwares_formatter,
        _authors_formatter,
        None,
        _image_formatter]
    # форматируем столбцы из данных модели и обратных связей
    column_labels = {
        'build_name' : 'название сборки',
        'inch' : 'дюйм',
        'hardwares' : 'Оборудование',
        'authors' : 'Авторы',
        'build_desc' : 'описание сборки',
        'build_image_id' : 'изображение сборки'}

    
    
    
    
    
    