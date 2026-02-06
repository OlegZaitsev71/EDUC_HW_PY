"""ДЗ по теме SQLAlchemy."""
# DB часть по бронированию авиарейсов

#from sqlalchemy import MetaData
from sqlalchemy import MetaData, Table, insert, select, update, and_
import sys
from hw10.db.hw10_zoa_db_engine import get_engine
from sqlalchemy.orm import sessionmaker, joinedload, join
from hw10.db.hw9_zoa_redis import getvar, setvar, decrvar, incrvar

# sys.path.append('../src')
engine = get_engine() 

metadata = MetaData()
metadata.reflect(bind=engine)
users_table = Table('users', metadata, autoload=True)
spfli_table = Table('spfli', metadata, autoload=True)
sflight_table = Table('sflight', metadata, autoload=True)
sbook_table = Table('sbook', metadata, autoload=True)
# hw10
scarr_table = Table('scarr', metadata, autoload=True)
#sbook_table = Table('sbook1', metadata, autoload=True)

def check_userid(userid) ->str:
    with engine.connect() as conn:
        stmt = select(users_table.c.username).where(users_table.c.id == userid) 
        for row in conn.execute(stmt):
            return row[0]
        return None

# hw10
def get_users() ->list:
    with engine.connect() as conn:
        stmt = select(users_table.c.id, users_table.c.username).where(users_table.c.is_active == True ) 
        users = conn.execute(stmt)
        return users

# hw10
def get_user_by_id(userid: int) ->str:
    with engine.connect() as conn:
        stmt = select(users_table.c.id, users_table.c.username).where(users_table.c.id == userid) 
        for row in conn.execute(stmt):
            return row
        return None

#hw10
def get_sbooks_by_userid(userid: int) ->str:
    with engine.connect() as conn:
        stmt = (
            select(
                sbook_table.c.bookid,
                scarr_table.c.carname,
                spfli_table.c.cityfr,
                spfli_table.c.airpfr,
                spfli_table.c.cityto,
                spfli_table.c.airpto,
                sbook_table.c.fldate,
                spfli_table.c.fltime,
                sflight_table.c.price,
                sflight_table.c.currency
            )
                .select_from(sbook_table
                            .join(sflight_table,   and_(sbook_table.c.carrid == sflight_table.c.carrid,
                                        sbook_table.c.connid == sflight_table.c.connid,
                                        sbook_table.c.fldate == sflight_table.c.fldate),
                                        isouter= True) 
                            .join(spfli_table, and_(sbook_table.c.carrid == spfli_table.c.carrid,
                                    sbook_table.c.connid == spfli_table.c.connid), 
                                    isouter= True) 
                            .join(scarr_table, and_(sbook_table.c.carrid == scarr_table.c.carrid ) , isouter= True )      
                                    )
                .where( sbook_table.c.userid == userid)
                .order_by(sbook_table.c.bookid.asc())
                )
        sbook_data = conn.execute(stmt)
        return sbook_data

#hw10
def create_new_bookid_db(sbook_data: dict):
    # sbook_data['userid']
    # sbook_data['carrid']
    # sbook_data['connid']
    # sbook_data['fldate']
    # sbook_data['sflight_seats']

    # Проверка наличия userid в БД
    if check_userid(sbook_data['userid']) is None:
        return {
            'success': False,
            'message': f'Пользователь {sbook_data['userid']} не авторизирован в БД!'
                }
    # Проверка наличия авиарейса на указанную дату
    sflight_data = read_sflight_hw10(sbook_data)
    if sflight_data is None:
        return {
            'success': False,
            'message': f'Нет авиарейса {sbook_data['connid']} на дату {sbook_data['fldate']}'
                }
    
    # Проверка наличия авиаброни на эту дату у userid
    if get_sbook_bookid(sbook_data) is not None:
        return {
            'success': False,
            'message': f'У пользователя {sbook_data['userid']} уже есть бронь на дату {sbook_data['fldate']}'
                }
    
    for row in sflight_data:
        if isinstance(row[4], int) and isinstance(row[5], int):
            # Определить число незанятых мест на рейсе
            seatfree = int(row[4] - row[5])
            sflight_seatmax = int(row[4])
            # Установить ключ в БД Redis, если он не установлен кем-то другим в параллельной сессии
            if getvar(str(row[1])) is None:
                setvar(str(row[1]), str(seatfree) )
            break

    # Проверка на овербукинг
    seatfree = int(getvar(sbook_data['connid']))
    if seatfree < sbook_data['sflight_seats']:
        return {
            'success': False,
            'message': f'Овербукинг: номер рейса {sbook_data['connid']}, доступных мест {seatfree}'
                }
    # Update Redis
    if decrvar(sbook_data['connid'], sbook_data['sflight_seats']):
        seatfree = int(getvar((sbook_data['connid'])))
        seatocc = sflight_seatmax - seatfree
        # Update DB
        if update_sflight(sbook_data['userid'], sbook_data['carrid'], sbook_data['connid'], sbook_data['fldate'], seatocc):
            bookid_data = get_sbook_bookid(sbook_data)
            for row in bookid_data:
                return {
                    'success': True,
                    'message': f'Обновление БД Redis & PostgreSQL выполнено успешно! Авиабронь {row}'
                    }
        else:
            incrvar(sbook_data['connid'], sbook_data['sflight_seats'])
            return {
                'success': False,
                'message': 'Ошибка обновления БД PostgreSQL!'
                }
    else:
        return {
                'success': False,
                'message': 'Ошибка обновления БД Redis!'
                }

def read_spfli_cities() ->list:
    with engine.connect() as conn:
        stmt = select(spfli_table.c.countryfr, spfli_table.c.cityfr, spfli_table.c.countryto, spfli_table.c.cityto)
        spfli_cities = conn.execute(stmt)
        return spfli_cities

def read_sflight_hw10(sflight_data: dict) ->list:
    with engine.connect() as conn:
        stmt = (
            select(
                sflight_table.c.carrid, 
                sflight_table.c.connid, 
                sflight_table.c.fldate,
                sflight_table.c.price,
                sflight_table.c.seatmax,
                sflight_table.c.seatocc             
                )
            .select_from(sflight_table)
            .where( sflight_table.c.carrid ==  sflight_data['carrid'], 
                    sflight_table.c.connid ==  sflight_data['connid'],
                    sflight_table.c.fldate == sflight_data['fldate'],
                    sflight_table.c.seatocc < sflight_table.c.seatmax )
            .order_by(sflight_table.c.price.asc())
        )
        sflight_data = conn.execute(stmt)
        return sflight_data
    
def read_sflight(cityfr, cityto, date_sflight) ->list:
    with engine.connect() as conn:
        stmt = (
            select(
                sflight_table.c.carrid, 
                sflight_table.c.connid, 
                sflight_table.c.fldate,
                sflight_table.c.price,
                sflight_table.c.seatmax,
                sflight_table.c.seatocc             
                )
            .select_from(sflight_table).join(spfli_table)
            .where(sflight_table.c.fldate == date_sflight, 
                    sflight_table.c.seatocc < sflight_table.c.seatmax,
                    spfli_table.c.cityfr == cityfr,
                    spfli_table.c.cityto == cityto)
            .order_by(sflight_table.c.price.asc())
        )
        sflight_data = conn.execute(stmt)
        return sflight_data
    
def update_sflight(userid, carrid, connid, fldate, seatocc) ->bool:
    with engine.connect() as conn:
        try:
            # update sbook
            conn.execute(insert(sbook_table).values(carrid=carrid, 
                                                connid=connid, 
                                                fldate=fldate,
                                                userid=userid))
            # update sflight
            conn.execute(update(sflight_table).values(seatocc=seatocc)
                        .where( sflight_table.c.carrid == carrid, 
                                sflight_table.c.connid == connid, 
                                sflight_table.c.fldate == fldate))
            conn.commit() 
            return True
        except Exception as e:
            conn.rollback()
            return False
                                                
def get_sbook_bookid(sbook_key: dict) ->list:
    with engine.connect() as conn:
        stmt = (
            select(sbook_table.c.bookid)
                .select_from(sbook_table)
                .where(sbook_table.c.carrid == sbook_key['carrid'],
                                                sbook_table.c.connid == sbook_key['connid'],
                                                sbook_table.c.fldate == sbook_key['fldate'],
                                                sbook_table.c.userid == sbook_key['userid']
                                                )
        )
        for row in conn.execute(stmt):
            return row
        return None
        


# todo