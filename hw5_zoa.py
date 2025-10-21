"""ДЗ №5 по теме <Работа с файлами и контекстными менеджерами в Python>."""  
# python hw5_zoa.py --path hw5_zoa_folder --report hw5_zoa_rep.xlsx
import argparse
from pathlib import Path
import os
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Alignment
from string import ascii_uppercase

parser = argparse.ArgumentParser(description='Разбор содержимого папки с отчетовм в файл')
parser.add_argument(
    # Полный ключ параметра
    '--path',
    # Краткое имя параметра
    '-p',
    # Тип параметра
    type=str,
    # Значение по умолчанию
    default='./hw5_zoa_folder',
    # Комментарий (показывается по ключу --help)
    help='Путь к анализируемой папке',
)
parser.add_argument(
    # Полный ключ параметра
    '--report',
    # Краткое имя параметра
    '-r',
    # Тип параметра
    type=str,
    # Значение по умолчанию
    default='./hw5_zoa_rep.xlsx',
    # Комментарий (показывается по ключу --help)
    help='Путь к файлу отчета',
)

# Чтение аргументов командной строки
arg_val = parser.parse_args()
hw5_zoa_folder = arg_val.path
hw5_zoa_rep = arg_val.report

# Проверка наличия папки в текущей директории
if not Path(hw5_zoa_folder).exists:
    raise FileNotFoundError(f'Папка {hw5_zoa_folder} не найдена!')

# Проверка расширения файла отчета
rep_file_ex_set = ['.docx', '.xlsx', '.pdf', '.csv', '.json']
rep_file_ex = Path(hw5_zoa_rep).suffix
if rep_file_ex not in rep_file_ex_set:
    raise FileNotFoundError(f'Файл {hw5_zoa_rep} не имеет нужного расширения!')

print('Аргументы вызова:')
print('Папка:', hw5_zoa_folder)
print('Файл отчета:', hw5_zoa_rep )

# _get_dir_content(path):
def _get_dir_content(path):
    """Функция генератор(внутренний вызов)."""  
    path_list_dir = Path(path)
    # for item in path_list_dir:
    for item in path_list_dir.iterdir():
        item_join_path = path_list_dir.joinpath(item)
        if os.path.isdir(item_join_path):
            yield item_join_path
            for sub_item in _get_dir_content(item_join_path ):
                yield sub_item
        else:
            yield item_join_path

# get_dir_content
def get_dir_content(path):
    """Функция генератор(внешний вызов)."""  
    for item in _get_dir_content(path):
        yield item

# Перебор папки с использованием генератора
path = Path(hw5_zoa_folder).absolute()
res_dir_gen = get_dir_content(path)
res_dir_lst = list(res_dir_gen)

# сохранаем в list с нужной детализацией
res_dir_content = list([])
for item in res_dir_lst:
    path = Path(item)
    datetime_out = datetime.fromtimestamp(path.stat().st_mtime)
    if not path.is_file() or path.suffix == '.zip':
        res_dir_content.append(['FOLDER:', item, datetime_out.strftime('%Y-%m-%d %H:%M:%S'), path.stat().st_size])
    elif path.is_file():
        res_dir_content.append(['FILE:', item, datetime_out.strftime('%Y-%m-%d %H:%M:%S'), path.stat().st_size])

#print(f'Содержимое папки: {hw5_zoa_folder}')
#for item in res_dir_content:
#    print(item)

# сохранение результата анализа в файл (2й параметр)
wb = Workbook()
ws = wb.active
ws.delete_cols(1,10)
ws.delete_rows(1,100)
ws.title = 'Содержимое папки'
hdr = ['Объект', 'Путь', 'Дата изменения', 'Размер(байт)']
ws.append(hdr)
for item in res_dir_content:
    sub_item_tot = list()
    index = int()
    for sub_item in item:
        match index:
            case 1:
                sub_item_tot.append(os.path.realpath(sub_item))
            case _:
                sub_item_tot.append(sub_item) 
        index += 1
    ws.append(sub_item_tot)

# попытка выравнивания нужных columns
for column in ascii_uppercase:
    if column == 'E':
        break
    match column:
        case 'B':
            ws.column_dimensions[column].width = 100
        case _:
            ws.column_dimensions[column].width = 25 

for row in ws[2:100]:
    for j in range(4):
        cell = row[j]
        cell.alignment = Alignment(horizontal='left')

# сохраняем изменения
try:
    wb.save(hw5_zoa_rep)
    wb.close()
    print(f'Данные успешно сохранены в файл: {hw5_zoa_rep}')
except Exception as e:  
    print(f'Что-то пошло не так: {e}') 




