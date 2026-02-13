#hw11
import numpy as np

# Числа с плавающей точкой  
arr_float = np.array([1.0, 2.5, 3.7], dtype=np.float64)

arr = np.array([[1, 2, 3], 
                [4, 5, 6]])

print(arr.ndim)    # 2 (количество осей/измерений)
print(arr.shape)   # (2, 3) (размеры по каждой оси)
print(arr.size)    # 6 (общее количество элементов)
print(arr.itemsize) 

print("\n" + "="*50 + "\n")

# Срезы
arr_2d = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])

print(arr_2d[0:2, 1:3])  # [2,3] [6,7] - создается View (не копия), т.е. указатель

# Fancy indexing
arr_3d = np.array([[1, 2, 3],
                    [4, 5, 6], 
                    [7, 8, 9]])

print(arr_3d[[0, 1, 2], [0, 1, 2]])  # [1 5 9] (диагональ)
# Маска
print(arr_3d[arr_3d > 3])
print(arr_3d[(arr_3d < 3) | (arr_3d > 5)])  # [1 2 6]  # создается копия

# Изменение по условию
arr = np.array([1, 2, 3, 4, 5, 6])
arr[arr % 2 == 0] = -1
arr[(arr > 2) & (arr < 5)] = 999
print(arr)

# Матричное умножение
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a @ b)           
print(np.dot(a, b))

# Broadcasting
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
                
result = arr + 10  # Скаляр расширяется до формы arr
# [[11 12 13]
#  [14 15 16]]

# ОСновные операции
# математические
    #  sin, exp, sqrt, log
# арифметические
    # add, multiply, power 
# тригонометрия
    # cos, tan
# сравнения
    # greater, equal
# агрегации
    # sum, min, std (стандартное отклонение), var (дисперсия), min, max
    # std**2 = var

arr_2d = np.array([[1, 2, 3],
                    [4, 5, 6]])

print(np.sum(arr_2d, axis=0)) # [5 7 9] - сумма по столбцам


# Манипуляции с массивами
# reshape, ravel - создают View
arr = np.arange(12)  # [0 1 2 3 4 5 6 7 8 9 10 11]
arr_2d = arr.reshape(3, 4)   # матрица 3x4

arr_2d = np.array([[1, 2], [3, 4]])
flat = arr_2d.ravel()  # [1 2 3 4] (view)

# flatten - создает копию
arr_2d = np.array([[1, 2], [3, 4]])
flat = arr_2d.flatten()  # [1 2 3 4] (копия)

# transpose() - транспонирование, замена строк на столбцы

# Объединение
# print(np.concatenate([a, b], axis=1))

# vstack, hstack - вретикальное, горизонтальное объединение
# Разделение - split, hsplit, vsplit

# Нормальное распределение
print(np.random.normal(10, 2, (2, 3)))  # Матрица 2x3 с mean=10, std=2