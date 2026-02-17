from Models.Sections import Sections
class SectionsController():
    """управление секциями, позже понять необходимость в данном коде!"""
    @classmethod
    def get_section_info(cls, section):
        sectionInfo = Sections.get_or_none(Sections.sectionName == section)
        return {
        'sectionName' : sectionInfo.sectionName,
        'sectionTitle' : sectionInfo.sectionTitle,
        'sectionDesc' : sectionInfo.sectionDesc,
        'sectionReq' : sectionInfo.sectionReq
        }
