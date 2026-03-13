from Models.Faq import *
class FaqController():
    @classmethod
    def add(cls, **kwargs):
        Faq.create(**kwargs)
    @classmethod
    def get(cls):
        return Faq.select()
    @classmethod
    def show(cls, id):
        return Faq.get_or_none(Faq.id == id)
    @classmethod
    def update(cls, id, **kwargs):
        for key, value in kwargs.items():
            Faq.update({key:value}).where(Faq.id == id).execute()
    @classmethod
    def delete(cls, id):
        Faq.delete().where(Faq.id == id).execute()
    @classmethod
    def get_listFaq(cls):
        pass
        






