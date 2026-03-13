class ModelsController():
    @classmethod
    def add(cls, **kwargs):
        return cls.model.create(**kwargs)
    @classmethod
    def get(cls):
        return cls.model.select()
    @classmethod
    def show(cls, id):
        return cls.model.get_or_none(cls.model.id == id)
    @classmethod
    def update(cls, id, **kwargs):
        for key, value in kwargs.items():
            cls.model.update({key:value}).where(cls.model.id == id).execute()
    @classmethod
    def delete(cls, id):
        return cls.model.delete().where(cls.model.id == id).execute()