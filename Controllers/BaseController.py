# # импорты 
# from playhouse.shortcuts import model_to_dict # playhouse поставляется с peewee
# class BaseController():
#     @classmethod
#     def get(cls):
#         return cls.model.select().execute()   
#     @classmethod
#     def get_desc(cls):
#         """desc: обратное направление"""
#         return cls.model.select().order_by(cls.model.id.desc())
#     @classmethod
#     def get_by_attr(cls, attr, val):
#         return cls.model.get_or_none(getattr(cls.model, attr) == val)
#     @classmethod
#     def modelRow_Dict(cls, row):
#         """конвентер строки модели в словарь"""
#         return model_to_dict(row, recurse=True)
#     @classmethod
#     def modelRows_toListDicts(cls, select):
#         """генератор списка из селектора"""
#         return [model_to_dict(row, recurse=True) for row in select]
#     @classmethod
#     def add(cls, **kwargs):
#         return cls.model.create(**kwargs)
    
#     @classmethod
#     def show(cls):
#         return cls.model.get_or_none()
#     @classmethod
#     def show_id(cls, id):
#         return cls.model.get_or_none(cls.model.id == id)
#     @classmethod
#     def update(cls, id, **kwargs):
#         for key, value in kwargs.items():
#             cls.model.update({key:value}).where(cls.model.id == id).execute()
#     @classmethod
#     def delete(cls, id):
#         return cls.model.delete().where(cls.model.id == id).execute()
# импорты 
from playhouse.shortcuts import model_to_dict # playhouse поставляется с peewee
from Models.Base import db
class BaseController():
    @classmethod
    def get(cls):
        if db.obj is None:
            return []
        try:
            return cls.model.select().execute()   
        except:
            return False
    @classmethod
    def get_desc(cls):
        """desc: обратное направление"""
        if db.obj is None:
            return []
        try:
            return cls.model.select().order_by(cls.model.id.desc())
        except:
            return False
    @classmethod
    def get_by_attr(cls, attr, val):
        if db.obj is None:
            return []
        try:
            return cls.model.get_or_none(getattr(cls.model, attr) == val)
        except:
            return False
    @classmethod
    def modelRow_Dict(cls, row):
        """конвентер строки модели в словарь"""
        if db.obj is None:
            return []
        try:
            return model_to_dict(row, recurse=True)
        except:
            return False
    @classmethod
    def modelRows_toListDicts(cls, select):
        """генератор списка из селектора"""
        if db.obj is None:
            return []
        try:
            return [model_to_dict(row, recurse=True) for row in select]
        except:
            return False
    @classmethod
    def add(cls, **kwargs):
        if db.obj is None:
            return []
        try:
            return cls.model.create(**kwargs)
        except:
            return False
        
    
    @classmethod
    def show(cls):
        if db.obj is None:
            return []
        try:
            return cls.model.get_or_none()
        except:
            return False
        
    @classmethod
    def show_id(cls, id):
        if db.obj is None:
            return []
        try:
            return cls.model.get_or_none(cls.model.id == id)
        except:
            return False
        
    @classmethod
    def update(cls, id, **kwargs):
        if db.obj is None:
            return []
        try:
            for key, value in kwargs.items():
                cls.model.update({key:value}).where(cls.model.id == id).execute()
        except:
            return False
        
    @classmethod
    def delete(cls, id):
        if db.obj is None:
            return []
        try:
            return cls.model.delete().where(cls.model.id == id).execute()
        except:
            return False