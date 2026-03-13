from Models.Sliders import Sliders
from Controllers.ModelsController import ModelsController
class SlidersController(ModelsController):
    model = Sliders
    @classmethod
    def get_listSlidersImages(cls):
        sliders_imgs = []
        for slider in cls.get():
            sliders_imgs.append(slider.image_id.src)
        return sliders_imgs






