# from Models.Builds import Builds
# from Models.Hardwares import Hardwares
from Models.Builds_authors import Builds_authors
from Controllers.PersonsController import PersonsController
from Controllers.BaseController import BaseController
class Builds_authorsController(BaseController):
    """управление данными персон"""
    model = Builds_authors
    @classmethod
    def get_by_build_id(cls, builds_id):
        builds_author = Builds_authors.get_or_none(Builds_authors.builds_id == builds_id)
        try:
            return PersonsController.get_cur_Person(builds_author.persons_id)['firstName']
        except AttributeError:
            return PersonsController.get_cur_Person(builds_author.persons_id)['lastName']
        except:
            print('ошибка: Builds_authorsController - неудачный опрос атрибута PersonsController.get_cur_Person(builds_author.persons_id)')



    