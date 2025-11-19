"""модуль для подлючения к базе данных"""
from peewee import *
# def connect_db():
#     return MySQLDatabase(
#         'drones',
#         user='drones207',
#         password='sakjdfhkjsadfhkjsdfs',
#         host='127.0.0.1',
#         port=3306)
def connect_db():
    return MySQLDatabase(
        'drones',
        user='drones',
        password='dsfkjlhgsdflkgl90890',
        host='192.168.0.102',
        port=3306)
# def connect_db():

#     return MySQLDatabase(
#         'OnVisp2_drones',
#         user='OnVisp2_drones',
#         password='111111',
#         host='10.11.13.118',
#         port=3306)
if __name__ == '__main__':
    connect_db().connect()


    # drones
    # dsfkjlhgsdflkgl90890

    # drones207
    # sakjdfhkjsadfhkjsdfs


