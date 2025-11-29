"""ДЗ по теме SQLAlchemy."""
# Заполнение данных таблиц на основе Faker
from faker import Faker
from sqlalchemy import MetaData, Table, insert, select
import sys
import hw9_zoa_db_engine
import string
import random
from datetime import datetime, date, timedelta

sys.path.append('../src')
engine = hw9_zoa_db_engine.get_engine() 
metadata = MetaData()
metadata.reflect(bind=engine)

fake = Faker('ru_RU')

def gen_random_chars(num_char):
    alpha = string.ascii_uppercase + string.digits
    chars = ''.join(random.choice(alpha) for _ in range(num_char))
    return chars

def gen_random_digit(num):
    alpha = string.digits
    chars = ''.join(random.choice(alpha) for _ in range(num))
    return chars

# users
users_table = Table('users', metadata, autoload=True)
with engine.begin() as conn:
    for i in range(1,6):
        conn.execute(insert(users_table).values(id=i, username=fake.name(), is_active=True))

scarr_table = Table('scarr', metadata, autoload=True)
with engine.begin() as conn:
    for j in range(1,6):
        match j:
            case 1:
                conn.execute(insert(scarr_table).values(carrid=j, carname='AEROFLOT'))
            case 2:
                conn.execute(insert(scarr_table).values(carrid=j, carname='AIR CHINA'))
            case 3:
                conn.execute(insert(scarr_table).values(carrid=j, carname='TURKISH AIRLINES'))
            case 4:
                conn.execute(insert(scarr_table).values(carrid=j, carname='QATAR AIRLINES'))
            case 5:
                conn.execute(insert(scarr_table).values(carrid=j, carname='PAN AMERICAN'))

# spfli
spfli_table = Table('spfli', metadata, autoload=True)
scarr_table = Table('scarr', metadata, autoload=True)
with engine.connect() as conn:
    stmt = select(scarr_table.c.carrid, scarr_table.c.carname)
    for row in conn.execute(stmt):
        #print(row[0])
        for _ in range(3):
            conn.execute(insert(spfli_table).values(carrid=row[0], 
                                                    connid=gen_random_digit(5), 
                                                    countryfr=fake.country(),
                                                    cityfr=fake.city_name(),
                                                    airpfr=gen_random_chars(3),
                                                    countryto=fake.country(),
                                                    cityto=fake.city_name(),
                                                    airpto=gen_random_chars(3),
                                                    fltime=fake.random_digit_not_null()))
            conn.commit()

# sflight
spfli_table = Table('spfli', metadata, autoload=True)
sflight_table = Table('sflight', metadata, autoload=True)
with engine.connect() as conn:
    stmt = select(spfli_table.c.carrid, spfli_table.c.connid)
    for row in conn.execute(stmt):
        #print(row)
        today = date.today()
        for i in range(1,6):
            calc_date = today + timedelta(days=i)
            r_price = random.uniform(50, 500)
            conn.execute(insert(sflight_table).values(carrid=row[0], 
                                        connid=row[1], 
                                        fldate=calc_date,
                                        price=round(r_price,2),
                                        currency='USD',
                                        seatmax=random.randint(10, 100),
                                        seatocc=random.randint(10, 100)))
            conn.commit()       