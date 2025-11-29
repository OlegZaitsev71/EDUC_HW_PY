"""ДЗ по теме SQLAlchemy."""
#Подключение к СУБД PostgreSQL

from sqlalchemy import create_engine, URL
from dotenv import dotenv_values
#import urllib.parse

def get_engine():
    config   = dotenv_values('.env')
    user     = config['POSTGRES_USER']
    password = config['POSTGRES_PASSWORD']
    host     = config['POSTGRES_HOST']
    port     = config['POSTGRES_PORT']
    database = config['POSTGRES_DB']
    
    # Диалект
    dialect  = 'postgresql'
    driver   = 'psycopg2'
    
# Подключение в более читаемом виде
    url_object = URL.create(
        f'{dialect}+{driver}',
        username=user,
        password=password,  # Неэкранированный пароль
        host=host,
        port=port,
        database=database)

    engine = create_engine(url_object, echo='debug')

    return engine