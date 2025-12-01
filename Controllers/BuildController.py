from Models.Builds import *
from Controllers.ImagesController import *
from Controllers.Builds_hardwaresController import *
from Controllers.Builds_authorsController import *
class BuildController():
    """
        управление данными таблицы расписание
    """
    @classmethod
    def get(cls):
        return Builds.select()
    @classmethod
    def add(cls, inch, build_desc, build_image_id):
        return Builds.create(
            inch=inch,
            build_desc=build_desc,
            build_image_id=build_image_id
        )
    @classmethod
    def delete(cls, id):
        return BuildController.delete().where(BuildController.id == id).execute()
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            BuildController.update({key:value}).where(BuildController.id == id).execute()
    
    @classmethod
    def getBuilds(cls):
        builds = BuildController.get()
        builds_list = []
        for build in builds:
            builds_dict = {}
            builds_dict['id'] = build.id
            builds_dict['inch'] = build.inch
            builds_dict['build_desc'] = build.build_desc
            builds_dict['build_image_src'] = ImagesController.show_id(build.build_image_id).src
            builds_dict['author'] = Builds_authorsController.get_by_build_id(build.id)
            builds_dict['hardwares_list'] = Builds_hardwaresController.get_by_build_id(build.id)
            builds_list.append(builds_dict)
        return builds_list
    