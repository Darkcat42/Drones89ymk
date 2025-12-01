from Models.Builds import *
from Models.Hardwares import *
from Models.Builds_hardwares import *
from Controllers.HardwaresController import *
class Builds_hardwaresController():
    """
        управление данными таблицы расписание
    """
    @classmethod
    def get(cls):
        return Builds_hardwares.select()
    @classmethod
    def add(cls, Hardwares_id, builds_id):
        Builds_hardwares.create(
            Hardwares_id = Hardwares_id,
            builds_id = builds_id 
        )
    @classmethod
    def get_by_build_id(cls, builds_id):
        hardwares_list = []
        for builds_hardware in Builds_hardwares.select().where(Builds_hardwares.builds_id == builds_id):
            hardwares_list.append(HardwaresController.get_cur_hardware(builds_hardware.Hardwares_id))
        return hardwares_list
    @classmethod
    def delete(cls, id):
        return Builds_hardwares.delete().where(Builds_hardwares.id == id).execute()
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Builds_hardwares.update({key:value}).where(Builds_hardwares.id == id).execute()
    