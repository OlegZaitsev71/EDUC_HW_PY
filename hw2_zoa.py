#hw2_zoa
import hw2_zoa_module

# 1 task
def todo(): pass    #заглушка

def todo1():
    str = 'Hello world!'
    return str

print(todo1())

class ToDoClass:
    def todo(self):
        my_str = 'Hello world again!'
        return my_str

c1 = ToDoClass()
print(c1.todo())

# 2 task
user_name = input('Привет! Укажи свое имя:')
user_age = input('Укажи свой возраст:')
print('Привет,', user_name, 'через 5 лет тебе будет', int(user_age)+5)

# 3 task
if True: 
    print('Hello') 

# 4 task
def test_func():
    lv_num = int(input('Введите число:'))
    if lv_num < 0 and (lv_num%2 == 0 or lv_num%3 == 0):
        lv_str = 'Negatine'
    elif lv_num > 0 and (lv_num%2 == 0 or lv_num%3 == 0):
        lv_str = 'Positive'
    else:
        lv_str = 'Zero'

    return lv_str

print(test_func())

# 5 task
my_range = range(10,20)
print( list(my_range) )
my_num = input('Введите число:')
if int(my_num) in my_range:
    print('Число из диапазона!')
elif int(my_num) not in my_range:
    print('Число не из диапазона!')
elif my_num is None:
    print('Это не число!')

# 6 task
my_cmd = input('Введите команду(start/stop/pause):')
match my_cmd:
    case 'start':
        print('Запуск')
    case 'stop':
        print('Останов')
    case 'pause':
        print('Пауза')
    case _:
        print('Незвестная команда')

# 7 task
true_psw = '1234'
while input('Введите пароль:') != true_psw:
    pass
else:
    print('Пароль верный!')

# моржовый оператор
while (true_psw := input('Введите пароль:')) != '1234':
    pass
else:
    print('Пароль верный!')

print('Квадрат числа от 1 до 5:')
for i in range(1,5):
    print('Квадрат числа:', i*i) 

# 8 task
try:
    my_num  = int(input('Введите число: '))
    my_div  = 10/my_num
    print('Результат деления', str(my_div))
except ValueError:
    print('Это не число')
except ZeroDivisionError as zdiv:  # noqa: F841
    print('Попытка деления на ноль!','Исключение: {str(zdiv)}')
    raise ValueError('Недопустимое значение!')
finally:
    print('Операция деления числа завершена!')

# 9 task
print('Попытка вызова функции из модуля')
hw2_zoa_module.hello()

#10 task
try:
    print('even') if int(input('Введите число: '))%2 == 0 else print('odd')
    my_num = int(input('Введите число: '))
    print('Это число!') if isinstance(my_num, int) else print('Это не число!')
except ValueError:
    print('Это не число!')
