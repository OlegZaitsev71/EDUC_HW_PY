"""ДЗ по теме SQLAlchemy."""
# DB часть по бронированию авиарейсов

#from sqlalchemy import MetaData
from sqlalchemy import MetaData, Table, insert, select, update
import sys
import hw9_zoa_db_engine

sys.path.append('../src')
engine = hw9_zoa_db_engine.get_engine() 

metadata = MetaData()
metadata.reflect(bind=engine)
users_table = Table('users', metadata, autoload=True)
spfi_table = Table('spfli', metadata, autoload=True)
sfight_table = Table('sflight', metadata, autoload=True)
sbook_table = Table('sbook', metadata, autoload=True)

def check_userid(userid) ->str:
    with engine.connect() as conn:
        stmt = select(users_table.c.username).where(users_table.c.id == userid) 
        for row in conn.execute(stmt):
            return row[0]
        return None

def read_spfli_cities() ->list:
    with engine.connect() as conn:
        stmt = select(spfi_table.c.countryfr, spfi_table.c.cityfr, spfi_table.c.countryto, spfi_table.c.cityto)
        spfli_cities = conn.execute(stmt)
        return spfli_cities

def read_sflight(cityfr, cityto, date_sflight) ->list:
    with engine.connect() as conn:
        stmt = (
            select(
                sfight_table.c.carrid, 
                sfight_table.c.connid, 
                sfight_table.c.fldate,
                sfight_table.c.price,
                sfight_table.c.seatmax,
                sfight_table.c.seatocc             
                )
            .select_from(sfight_table).join(spfi_table)
            .where(sfight_table.c.fldate == date_sflight, 
                    sfight_table.c.seatocc < sfight_table.c.seatmax,
                    spfi_table.c.cityfr == cityfr,
                    spfi_table.c.cityto == cityto)
            .order_by(sfight_table.c.price.asc())
        )
        sflight_data = conn.execute(stmt)
        return sflight_data
    
def update_sflight(userid, carrid, connid, fldate, seatocc):
    with engine.connect() as conn:
        # update sbook
        conn.execute(insert(sbook_table).values(carrid=carrid, 
                                                connid=connid, 
                                                fldate=fldate,
                                                userid=userid))
        # update sflight
        conn.execute(update(sfight_table).values(seatocc=seatocc)
                        .where( sfight_table.c.carrid == carrid, 
                                sfight_table.c.connid == connid, 
                                sfight_table.c.fldate == fldate))
        conn.commit() 
                                                



# todo