from Models.Hardwares import *
class HardwaresController():
    """управление данными оборудования"""
    @classmethod
    def get(cls):
        return Hardwares.select()
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
    def add(cls, category, name, count, cost, sourceName, sourceUrl):
        Hardwares.create(
            category = category,
            name = name,
            count = count,
            cost = cost,
            sourceName = sourceName,
            sourceUrl = sourceUrl
        )
    @classmethod
    def delete(cls, id):
        return Hardwares.delete().where(Hardwares.id == id).execute()
    @classmethod
    def show(cls, id):
        return Hardwares.get_or_none(Hardwares.id == id)
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
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Hardwares.update({key:value}).where(Hardwares.id == id).execute()
    # @classmethod
    # def getNew_dict(cls, id):
    #     new = NewsController.show(id)
    #     new_dict = {}
    #     new_dict['id'] = new.id
    #     new_dict['title'] = new.title
    #     new_dict['news_desc'] = new.news_desc
    #     new_dict['date'] = new.date
    #     new_dict['image_src'] = new.image_id.src
    #     return new_dict

    # @classmethod
    # def getLast_dict(cls):
    #     new = News.select().order_by(News.id.desc())
    #     new_dict = {}
    #     try:
    #         new_dict['id'] = new[0].id
    #         new_dict['title'] = new[0].title
    #         new_dict['news_desc'] = new[0].news_desc
    #         new_dict['date'] = new[0].date
    #         new_dict['image_src'] = new[0].image_id.src
    #     except IndexError:
    #         new_dict['id'] = 1
    #         new_dict['title'] = 'Новостей пока нет'
    #         new_dict['news_desc'] = 'Здесь будет текст будущих вестей'
    #         new_dict['date'] = datetime.datetime.date(datetime.datetime.now())
    #         new_dict['image_src'] = 'место под изображение'
    #     return new_dict