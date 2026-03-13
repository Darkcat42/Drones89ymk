from Models.Hardwares import Hardwares
from Controllers.ModelsController import ModelsController
class HardwaresController(ModelsController):
    """управление данными оборудования"""
    model = Hardwares
    @classmethod
    def get_by_categoty(cls, category):
        return Hardwares.select().where(Hardwares.category == category)
    @classmethod
    def get_hardwaresCategoty(cls, category):
        hardwares_list = []
        for hardware in HardwaresController.get_by_categoty(category):
            hardwares_dict = {}
            hardwares_dict['id'] = hardware.id
            hardwares_dict['name'] = hardware.name
            hardwares_dict['count'] = hardware.count
            hardwares_dict['cost'] = hardware.cost
            hardwares_dict['sourceName'] = hardware.sourceName
            hardwares_dict['sourceUrl'] = hardware.sourceUrl
            hardwares_list.append(hardwares_dict)
        return hardwares_list
    
    @classmethod
    def get_cur_hardware(cls, id):
        hardware = HardwaresController.show(id)

        hardwares_dict = {}
        hardwares_dict['id'] = hardware.id
        hardwares_dict['name'] = hardware.name
        hardwares_dict['count'] = hardware.count
        hardwares_dict['cost'] = hardware.cost
        hardwares_dict['sourceName'] = hardware.sourceName
        hardwares_dict['sourceUrl'] = hardware.sourceUrl

        return hardwares_dict
    @classmethod
    def get_hardwares(cls):
        hardwares_list = []
        for hardware in HardwaresController.get():
            hardwares_dict = {}
            hardwares_dict['id'] = hardware.id
            hardwares_dict['name'] = hardware.name
            hardwares_dict['count'] = hardware.count
            hardwares_dict['cost'] = hardware.cost
            hardwares_dict['sourceName'] = hardware.sourceName
            hardwares_dict['sourceUrl'] = hardware.sourceUrl
            hardwares_list.append(hardwares_dict)
        return hardwares_list
    