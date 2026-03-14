from Models.Builds import Builds
from Controllers.ImagesController import ImagesController
from Controllers.Builds_hardwaresController import Builds_hardwaresController
from Controllers.Builds_authorsController import Builds_authorsController
from Controllers.ModelsController import ModelsController
class BuildController(ModelsController):
    model = Builds
    """управление данными cборок с дронами"""
    @classmethod
    def getBuilds(cls):
        builds = BuildController.get()
        builds_list = []
        for build in builds:
            builds_dict = {}
            builds_dict['id'] = build.id
            builds_dict['inch'] = build.inch
            builds_dict['build_desc'] = build.build_desc
            builds_dict['build_image_src'] = ImagesController.show(build.build_image_id).src
            builds_dict['author'] = Builds_authorsController.get_by_build_id(build.id)
            builds_dict['hardwares_list'] = Builds_hardwaresController.get_by_build_id(build.id)
            builds_list.append(builds_dict)
        return builds_list
    