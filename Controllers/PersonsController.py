from Models.Persons import Persons
from Models.Persons_types import *
from Controllers.ImagesController import ImagesController
from Controllers.ModelsController import ModelsController
class PersonsController(ModelsController):
    model = Persons
    """управление данными персон"""
    @classmethod
    def getPersons(cls):
        persons = PersonsController.get()
        persons_list = []
        for person in persons:
            
            persons_dict = {}
            persons_dict['id'] = person.id
            persons_dict['persons_types_id'] = person.persons_types_id
            persons_dict['images_src'] = ImagesController.show(person.images_id).src
            persons_dict['firstName'] = person.firstName
            persons_dict['lastName'] = person.lastName
            persons_dict['person_desc'] = person.person_desc
            persons_list.append(persons_dict)
        return persons_list
    @classmethod
    def get_cur_Person(cls, id):
        try:
            person = PersonsController.show(id)
            persons_dict = {}
            persons_dict['id'] = person.id
            persons_dict['persons_types_id'] = person.persons_types_id
            persons_dict['images_id'] = person.images_id
            persons_dict['firstName'] = person.firstName
            persons_dict['lastName'] = person.lastName
            persons_dict['person_desc'] = person.person_desc 
            return persons_dict
        except AttributeError:
            pass
   