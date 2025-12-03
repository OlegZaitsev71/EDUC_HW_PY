"""ДЗ по теме SQLAlchemy."""
# Клиентская часть по бронированию авиарейсов

from prompt_toolkit.shortcuts import choice
import datetime
import sys
import hw9_zoa_sbook_db
import hw9_zoa_redis

sys.path.append('../src')

def check_userid(userid) ->str:
    if not isinstance(userid, int):
        return None
    username = hw9_zoa_sbook_db.check_userid(userid)
    return username

def check_sflight_connid(sflight_data_list, sflight_connid) ->bool:
    for row in sflight_data_list:
        return int(row[1]) == sflight_connid


# Проверка авторизации пользователя
userid = int(input('Введите ID пользователя для бронирования:'))
username = check_userid(userid)
if username is None:
    print(f'Пользователь {userid} не авторизирован!')
    pass

print(f'Добрый день, {username}!')

# Чтение spfli
spfli_cityfr_list = []
spfli_cityto_list = []
spfli_cities = hw9_zoa_sbook_db.read_spfli_cities()
# Сформировать список кортежей для выбора cityfr, cityto
for row in spfli_cities:
    new_city = ()
    new_city += (row[1],)
    desc = (row[1], row[0])
    new_city += (', '.join(desc),)
    spfli_cityfr_list.append(new_city)
    new_city = ()
    new_city += (row[3],)
    desc = (row[3], row[2])
    new_city += (', '.join(desc),)
    spfli_cityto_list.append(new_city)

# Выбор города&страны отправления/назначения
cityfr = choice(  
    message='Выберите город отправления:',  
    options=spfli_cityfr_list,
)  
cityto = choice(  
    message='Выберите город назначения:',  
    options=spfli_cityto_list,
)

print(f'cityfr: {cityfr}')
print(f'cityto: {cityto}')

#  Ввод даты рейса
date_str = input('Введите дату вылета (dd/mm/yyyy)\n')
date_sflight = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
print(date_sflight)

# доступные рейсы
sflight_data_list = []
sflight_data = hw9_zoa_sbook_db.read_sflight(cityfr, cityto, date_sflight)
for row in sflight_data:
    print(f'Доступные рейсы(carrid,connid,fldate,price,seatmax,seatocc): {row}')
    # Добавление ключа <Номер рейса> : <Кол-во свободных мест> в DB Redis
    if isinstance(row[4], int) and isinstance(row[5], int):
        seatfree = row[4] - row[5]
        hw9_zoa_redis.setvar(str(row[1]), str(seatfree) )
    sflight_data_list.append(tuple(row))

my_cmd = input('Начать бронирование[Y,N]:')
match my_cmd:
    case 'Y':
        print('Запуск бронирования, выбор доступных авиарейсов:')
    case 'N':
        print('Отменена бронирования, выход')
        sys.exit()   # SystemExit
    case _:
        print('Незвестная команда')
        sys.exit()  # SystemExit

sflight_connid = int(input('Укажите номер рейса из доступных:'))
if not check_sflight_connid(sflight_data_list, sflight_connid):
    print(f'Неверный номер рейса {sflight_connid}')
    sys.exit()

for row in sflight_data_list:
    if isinstance(row[1], int) and row[1] == int(sflight_connid):
        sflight_carrid = int(row[0])
        sflight_seatmax = int(row[4])

# в БД PostgreSQL сделал поле sbook-bookid как счетчик: nextval('table_id_seq'::regclass)
sflight_connid_seats = int(input('Укажите число мест, рейс {sflight_connid}:'))
if sflight_connid_seats > 0:
    # update Redis
    if hw9_zoa_redis.decrvar(sflight_connid, sflight_connid_seats):
        seatfree = int(hw9_zoa_redis.getvar(sflight_connid))
        seatocc = sflight_seatmax - seatfree
        # update DB
        try:
            hw9_zoa_sbook_db.update_sflight(userid, sflight_carrid, sflight_connid, date_sflight, seatocc)
            print('Обновление БД Redis & PostgreSQL выполнено успешно!')
        except Exception as e:  
            print(f'Ошибка обновления БД: {e}') 
    else:
        print('Ошибка обновления БД Redis!')