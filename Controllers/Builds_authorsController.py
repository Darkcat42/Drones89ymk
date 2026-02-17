from Models.Builds import *
from Models.Hardwares import *
from Models.Builds_authors import *
from Controllers.PersonsController import *
class Builds_authorsController():
    """управление данными персон"""
    @classmethod
    def get(cls):
        return Builds_authors.select()
    @classmethod
    def add(cls, persons_id, builds_id):
        Builds_authors.create(
            persons_id = persons_id,
            builds_id = builds_id
        )
    @classmethod
    def get_by_build_id(cls, builds_id):
        builds_author = Builds_authors.get_or_none(Builds_authors.builds_id == builds_id)
        try:
            return PersonsController.get_cur_Person(builds_author.persons_id)['firstName']
        except AttributeError:
            return PersonsController.get_cur_Person(builds_author.persons_id)['lastName']
        except:
            print('ошибка: Builds_authorsController - неудачный опрос атрибута PersonsController.get_cur_Person(builds_author.persons_id)')
    @classmethod
    def delete(cls, id):
        return Builds_authors.delete().where(Builds_authors.id == id).execute()
    @classmethod
    def update(cls, id, **kwargs):
        Builds_authors.update(**kwargs).where(Builds_authors.id == id).execute()
    # @classmethod
    # def update(cls, id, **filds):
    #     for key, value in filds.items():
    #         Builds_authors.update({key:value}).where(Builds_authors.id == id).execute()


    