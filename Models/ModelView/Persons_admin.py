from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Persons_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
            if 'name' not in kwargs:
                kwargs['name'] = 'Персоны'
            super().__init__(model, *args, **kwargs)
    column_labels = {
        'persons_types_id' : 'тип персоны',
        'images_id' : 'картинка',
        'firstName': 'имя',
        'lastName': 'фамилия',
        'person_desc': 'описание персоны'
    }
    def _image_formatter(view, context, model, name):
        image_src = model.images_id.src
        if not image_src:
            return ""
        return Markup(f'<img src="../../{image_src}" class="img-fluid fsi lazy" alt="...">')
    def _personType_formatter(view, context, model, name):
        persons_type = model.persons_types_id.type
        if not persons_type:
            return ""
        return Markup(f'<a href="/admin/persons_types/">{persons_type}</a>') 
    column_formatters = {
        'images_id': _image_formatter,
        'persons_types_id': _personType_formatter,
    }
#     """
#     модель 
#     """
#     id = PrimaryKeyField()
#     persons_types_id = ForeignKeyField(Persons_types, backref='persons_types_id')
#     images_id = ForeignKeyField(Images)
#     firstName = CharField()
#     lastName = CharField()
#     person_desc = TextField()

#     def __str__(self):
#         return self.firstName +' '+ self.lastName
    
# if __name__ == '__main__':
#     connect_db().create_tables([Persons, Persons_types, Images])