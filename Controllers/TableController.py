from Models.Users import *
class TableController():
    @classmethod
    def add(cls, username, login, password, role_id):
        Users.create(
            username=username,
            login=login,
            password=password,
            role_id=role_id
        )
    @classmethod
    def get(cls):
        return Users.select()
    @classmethod
    def get_by_login(cls, search_login):
        return Users.get_or_none(Users.login==search_login)
    @classmethod
    def show(cls, id):
        return Users.get_or_none(id)
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Users.update({key:value}).where(Users.id == id).execute()
    @classmethod
    def delete(cls, id):
        Users.delete().where(Users.id == id).execute()
if __name__ == '__main__':
    pass




