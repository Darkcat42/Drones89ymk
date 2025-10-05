# IMPORTS
# from pickle import PROTO
# from telnetlib import AUTHENTICATION
# from tokenize import endpats

# import bcrypt
from Models.Paragraphs import *
class ParagraphsController():
# CLS METHOD FOR ADD USER
    # @classmethod
    # def add(cls, username, login, password, role_id):
    #     Users.create(
    #         username=username,
    #         login=login,
    #         password=password,
    #         role_id=role_id
    #     )
# CLS METHOD USER RECORD GETTER ALL
    @classmethod
    def get(cls):
        return Paragraphs.select()

# CLS METHOD USER RECORD GETTER WITH LOGIN
    @classmethod
    def get_by_login(cls, search_id):
        return Paragraphs.get_or_none(Paragraphs.id==search_id)

# # CLS METHOD USER RECORD OR NONE GETTER
#     @classmethod
#     def show(cls, id):
#         return Users.get_or_none(id)

# # CLS METHOD UPDATE RECORD WITH ID
#     @classmethod
#     def update(cls, id, **filds):
#         for key, value in filds.items():
#             Users.update({key:value}).where(Users.id == id).execute()

# # CLS METHOD DELETE RECORD WITH ID
#     @classmethod
#     def delete(cls, id):
#         Users.delete().where(Users.id == id).execute()

# CODE EXECUTION ZONE
if __name__ == '__main__':
    pass