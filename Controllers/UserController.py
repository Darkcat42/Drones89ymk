from Models.Users import *
class UsersController():
# CLS METHOD FOR ADD USER
    @classmethod
    def add(cls, username, login, password, role_id):
        Users.create(
            username=username,
            login=login,
            password=password,
            role_id=role_id
        )
# CLS METHOD USER RECORD GETTER ALL
    @classmethod
    def get(cls):
        return Users.select()

# CLS METHOD USER RECORD GETTER WITH LOGIN
    @classmethod
    def get_by_login(cls, search_login):
        return Users.get_or_none(Users.login==search_login)

# CLS METHOD USER RECORD OR NONE GETTER
    @classmethod
    def show(cls, id):
        return Users.get_or_none(id)

# CLS METHOD UPDATE RECORD WITH ID
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Users.update({key:value}).where(Users.id == id).execute()

# CLS METHOD DELETE RECORD WITH ID
    @classmethod
    def delete(cls, id):
        Users.delete().where(Users.id == id).execute()

# CLS METHOD CREATE USER FOR REGISTRATION
#     @classmethod
#     def registration(cls, username, login, password, role):
#         # пароль надо захэшировать
#         hashpassword = hashpw(password.encode('utf-8'), bcrypt.gensalt())
#         Users.create(username=username, login=login, password=hashpassword, role_id=role)

# CLS METHOD CHECK USER FOR AUTHENTICATION
#     @classmethod
#     def auch(cls, login, passwd):
#         if Users.get_or_none(Users.login == login) != None:
#             # SALT
#             salt = bcrypt.gensalt()
#
#             # GET USER PASSWORD FROM DB
#
#             exist_passwd = Users.get_or_none(Users.login == login).password
#             print(exist_passwd)
#             exist_passwd = exist_passwd.encode('utf-8')
#             # PASSWORD HASHING
#             hspassword = bcrypt.hashpw(passwd.encode('utf-8'), salt)
#
#             if bcrypt.checkpw(exist_passwd, hspassword):
#                 return True
#             else:
#                 return False
#         return False
        #     if checkpw(password.encode('utf-8'), hspassword.encode('utf-8')):
        #         return True
        # return False
    # @classmethod
    # def auch(cls, login, password):
    #     if Users.get_or_none(Users.login == login) != None:
    #         hspassword = Users.get_or_none(Users.login == login).password
    #         if checkpw(password.encode('utf-8'), hspassword.encode('utf-8')):
    #             return True
    #     return False
        #     if Users.get_or_none(Users.login == login).password == password:
        #         return True
        # else:
        #     return False
# CODE EXECUTION ZONE
if __name__ == '__main__':

    print('таблица')
    print(Users)
    print('поля в таблице которые имеют логин')
    print(Users.login)
    print('запись которая имеет искомый логин')
    print(Users.login == 'admin')

    # DRAW LINE
    for i in range(0, 15):
        print('\033[31m', end='')
        print('_______', end='')
    print('\033[m', '\n')

    # USERS ALL RECORD GETTER
    for users in UsersController.get():
        print(
            # color code start for text (33m - yellow, 36 - aqua)
            '\033[36m',
            'All record getter: ',
            '\n',
            '   ',
            users.id,
            users.login,
            users.password,
            users.role_id,
            # color code end for text (0m - reset)
            '\033[0m',
            '\n',
            sep=' | ')

    # DRAW LINE
    for i in range(0, 15):
        print('\033[31m',end='')
        print('_______', end='')
    print('\033[m', '\n')

    # USER RECORD WITH LOGIN GETTER
    # admin = UsersController.get_by_login('admin')
    # print(admin.login)





