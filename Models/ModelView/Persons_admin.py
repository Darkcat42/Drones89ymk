from flask_admin.contrib.peewee import ModelView
from markupsafe import Markup # для шаблонизатора, обозначение безопасного html
from flask import url_for
class Persons_admin(ModelView):
    def __init__(self, model, *args, **kwargs):
            if 'name' not in kwargs:
                kwargs['name'] = 'Персоны'
            super().__init__(model, *args, **kwargs)
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