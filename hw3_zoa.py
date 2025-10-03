# hw3_zoa
from collections import Counter

# 1 task
print('1. Определить вхождение элементов списка с учетом дубликатов:')
my_total = int()
my_list1 = list([1, 2, 3, 3, 4])
my_list2 = list([1, 2, 3, 7, 4, 3])
print('list1', my_list1)
print('list2', my_list2)
my_list1_val_count = Counter(my_list1)
my_list2_val_count = Counter(my_list2)
my_list1_val_common = my_list1_val_count.most_common()
my_list2_val_common = my_list2_val_count.most_common()
print('list1_val_common', my_list1_val_common)
print('list2_val_common', my_list2_val_common)
for i in my_list1_val_common:
    if i in my_list2_val_common:
        my_total += 1 
print('Результат:', my_total == len(my_list1_val_common))

# a new example
print('2й пример')
my_total = int()
my_list1 = list([1, 2, 3, 3, 4, 3])
print('list1', my_list1)
print('list2', my_list2)
my_list1_val_count = Counter(my_list1)
my_list2_val_count = Counter(my_list2)
my_list1_val_common = my_list1_val_count.most_common()
my_list2_val_common = my_list2_val_count.most_common()
print('list1_val_common', my_list1_val_common)
print('list2_val_common', my_list2_val_common)
for i in my_list1_val_common:
    if i in my_list2_val_common:
        my_total += 1 
print('Результат:', my_total == len(my_list1_val_common))

# 2 task
i = int()
print('2. Изменить значения списков между собой')
my_list1 = list([1, 2, 3, 3, 8, 4])
my_list2 = list([5, 3, 6, 7, 7, 1])
print('list1', my_list1, id(my_list1))
print('list2', my_list2, id(my_list2))
i=0
for my_list1_item in my_list1:
    try:
        my_list2_item = my_list2[i]
        my_list2[i] = my_list1_item
        my_list1[i] = my_list2_item 
    except IndexError:
        print('Ошибка обращения к элементу списка!')
    finally:
        i+=1
# my_list1, my_list2 = my_list2, my_list1
print('Результат замены:')
print('list1', my_list1, id(my_list1))
print('list2', my_list2, id(my_list2))

# 3 task 
print('3. Попытка перемножения 2-х матриц 3x3')
m2_col_num = int()
m1_row_num = int()
m1 = ((1, 2, 3), (2, 3, 4), (3,4,5)) 
m2 = ((2, 3, 4), (3, 4, 5), (4, 5, 6)) 
mr = list([[0,0,0], [0,0,0], [0,0,0]])
# без проверки на корректность размерности матриц
m1_row_num = 0
for m1_row in m1:
    m1_row_list = list(m1_row)
    m2_col_num = 0
    while m2_col_num < len(m2):
        m2_col_curr = int()
        for m1_row_cell in m1_row_list:
            try:
                mr[m1_row_num][m2_col_num] = mr[m1_row_num][m2_col_num] + m1_row_cell * m2[m2_col_curr][m2_col_num]
                m2_col_curr += 1
            except TypeError:
                print('Ошибка обращения к элементу матрицы!')
        m2_col_num += 1
    m1_row_num += 1

print('m1', m1)
print('m2', m2)
print('Результат:', mr)

print('V2. Умножение матрицы 3х3 на 3х1')
# с проверкой размерности при перемножении матриц
m2 = ((2), (3), (4))
mr = list()
m1_row_num = 0
for m1_row in m1:
    m1_row_list = list(m1_row)
    m2_col_num = 0
    m2_col_list = list()
    m2_col_list.append(m2[0])
    if len(m1_row_list) != len(m2):
        print('Некорректная размерность при умножении матриц m1 x m2 !')
        exit(0)
    while m2_col_num < len(m2_col_list):
        m2_col_curr = int()
        mr_cell_value = int()
        for m1_row_cell in m1_row_list:
            try:
                mr_cell_value  = mr_cell_value  + m1_row_cell * m2[m2_col_curr]
            except TypeError:
                print('Ошибка обращения к элементу матрицы m2!')
            m2_col_curr += 1
        try:
            mr_cell_list = list()
            mr_cell_list.append(mr_cell_value)
            mr.insert(m1_row_num, mr_cell_list)
        except TypeError:
            print('Ошибка обращения к элементу матрицы mr!')
        m2_col_num += 1
    m1_row_num += 1

print('m1', m1)
print('m2', m2)
print('Результат:', mr)

