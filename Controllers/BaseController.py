# импорты 
from playhouse.shortcuts import model_to_dict # playhouse поставляется с peewee
class BaseController():
    @classmethod
    def get(cls):
        return cls.model.select().execute()   
    @classmethod
    def get_desc(cls):
        """desc: обратное направление"""
        return cls.model.select().order_by(cls.model.id.desc())
    @classmethod
    def get_by_attr(cls, attr, val):
        return cls.model.get_or_none(getattr(cls.model, attr) == val)
    @classmethod
    def modelRow_Dict(cls, row):
        """конвентер строки модели в словарь"""
        return model_to_dict(row, recurse=True)
    @classmethod
    def modelRows_toListDicts(cls, select):
        """генератор списка из селектора"""
        return [model_to_dict(row, recurse=True) for row in select]
    @classmethod
    def add(cls, **kwargs):
        return cls.model.create(**kwargs)
    
    @classmethod
    def show(cls):
        return cls.model.get_or_none()
    @classmethod
    def show_id(cls, id):
        return cls.model.get_or_none(cls.model.id == id)
    @classmethod
    def update(cls, id, **kwargs):
        for key, value in kwargs.items():
            cls.model.update({key:value}).where(cls.model.id == id).execute()
    @classmethod
    def delete(cls, id):
        return cls.model.delete().where(cls.model.id == id).execute()