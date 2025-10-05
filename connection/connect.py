from peewee import *
def connect_db():
    return MySQLDatabase(
        'drones',
        user='drones',
        password='dsfkjlhgsdflkgl90890',
        host='192.168.0.102',
        port=3306)
if __name__ == '__main__':
    connect_db().connect()


    # drones
    # dsfkjlhgsdflkgl90890