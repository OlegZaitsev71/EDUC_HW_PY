"""ДЗ по теме SQLAlchemy."""
# Подключение к резидентной БД Redis из Python

import redis

POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

def getvar(variable_name):
    my_server = redis.Redis(connection_pool=POOL)
    response = my_server.get(variable_name)
    return response

def setvar(variable_name, variable_value):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.set(variable_name, variable_value)

# test
#setvar('zoa_key1', 'zoa_key1_val')
#print(getvar('zoa_key1'))