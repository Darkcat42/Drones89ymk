# from Models.Builds import Builds
# from Models.Hardwares import Hardwares
from Models.Builds_hardwares import Builds_hardwares
from Controllers.HardwaresController import HardwaresController
from Controllers.ModelsController import ModelsController
class Builds_hardwaresController(ModelsController):
    """управление набором оборудования для конкретной сборки (каждой сборки)"""
    model = Builds_hardwares
    @classmethod
    def get_by_build_id(cls, builds_id):
        hardwares_list = []
        for builds_hardware in Builds_hardwares.select().where(Builds_hardwares.builds_id == builds_id):
            hardwares_list.append(HardwaresController.get_cur_hardware(builds_hardware.Hardwares_id))
        return hardwares_list

    