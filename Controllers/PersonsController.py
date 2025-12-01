from Models.Persons import *
from Models.Persons_types import *
from Controllers.ImagesController import ImagesController
class PersonsController():
    """
        управление данными таблицы расписание
    """
    @classmethod
    def get(cls):
        return Persons.select()
    @classmethod
    def add(cls, persons_types_id, images_id, firstName, lastName, person_desc):
        Persons.create(  
            persons_types_id = persons_types_id,
            images_id = images_id,
            firstName = firstName,
            lastName = lastName,
            person_desc = person_desc
        )
    @classmethod
    def delete(cls, id):
        return Persons.delete().where(Persons.id == id).execute()
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Persons.update({key:value}).where(Persons.id == id).execute()
    @classmethod
    def getPersons(cls):
        persons = PersonsController.get()
        persons_list = []
        for person in persons:
            
            persons_dict = {}
            persons_dict['id'] = person.id
            persons_dict['persons_types_id'] = person.persons_types_id
            persons_dict['images_src'] = ImagesController.show_id(person.images_id).src
            persons_dict['firstName'] = person.firstName
            persons_dict['lastName'] = person.lastName
            persons_dict['person_desc'] = person.person_desc
            persons_list.append(persons_dict)
        return persons_list
    @classmethod
    def show(cls, id):
        return Persons.get_or_none(Persons.id == id)
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
    # @classmethod
    # def getNew_dict(cls, id):
    #     new = NewsController.show(id)
    #     new_dict = {}
    #     new_dict['id'] = new.id
    #     new_dict['title'] = new.title
    #     new_dict['news_desc'] = new.news_desc
    #     new_dict['date'] = new.date
    #     new_dict['image_src'] = new.image_id.src
    #     return new_dict

    # @classmethod
    # def getLast_dict(cls):
    #     new = News.select().order_by(News.id.desc())
    #     new_dict = {}
    #     try:
    #         new_dict['id'] = new[0].id
    #         new_dict['title'] = new[0].title
    #         new_dict['news_desc'] = new[0].news_desc
    #         new_dict['date'] = new[0].date
    #         new_dict['image_src'] = new[0].image_id.src
    #     except IndexError:
    #         new_dict['id'] = 1
    #         new_dict['title'] = 'Новостей пока нет'
    #         new_dict['news_desc'] = 'Здесь будет текст будущих вестей'
    #         new_dict['date'] = datetime.datetime.date(datetime.datetime.now())
    #         new_dict['image_src'] = 'место под изображение'
    #     return new_dict