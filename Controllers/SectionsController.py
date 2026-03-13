from Models.Sections import Sections
from Controllers.ModelsController import ModelsController
class SectionsController(ModelsController):
    model = Sections
    """управление данными секций"""
    @classmethod
    def get_section_info(cls, section):
        sectionInfo = Sections.get_or_none(Sections.sectionName == section)
        return {
        'sectionName' : sectionInfo.sectionName,
        'sectionTitle' : sectionInfo.sectionTitle,
        'sectionDesc' : sectionInfo.sectionDesc,
        'sectionReq' : sectionInfo.sectionReq
        }
