import random 
import string 
import math

# 1 task case
n = 1000 
n_word = 10 
actions = ('upper', 'reverse', 'double', 'del_digits', 'del_even', 'replace') 
text = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)]) 

# 1 task 
print('Строка текста:', text)
print(f'Число слов: {n_word}')
print(f'Действия : {actions}')

def my_func1(iv_text:str, iv_n_word:int, iv_actions:tuple) ->string:
    """Пример реализации функции для task 1."""   
    def get_randint(x:int, y:int):
        return lambda: random.randint(x, y)
    
    def get_word_list(iv_text:str, iv_n_word:int) ->list:
        lv_word_lst = list()
        lv_pos_start = int()
        lv_pos_end = int()
        lv_n_word = int()
        while lv_pos_end <= len(iv_text):
            randint_func = get_randint(1,20)
            lv_num_pos = randint_func()
            try:
                lv_pos_end = lv_pos_start + lv_num_pos
                if lv_pos_end <= len(iv_text):
                    if lv_n_word < iv_n_word: 
                        lv_word_lst.append(iv_text[lv_pos_start:lv_pos_end])
                lv_pos_start = lv_pos_start + lv_num_pos + 1
                lv_n_word += 1
            except IndexError:
                pass
        return lv_word_lst
    
    word_list = get_word_list(iv_text = iv_text, iv_n_word = iv_n_word)
    # print(word_list)
    i = int()
    for word in word_list:
        exec_cmd = iv_actions[i]
        i = i+1 if i < len(iv_actions)-1 else 0
        new_word = str()
        match exec_cmd:
            case 'upper':
                new_word = str(word).upper()
                print(f'upper: {str(word)} {str(new_word)}')
                # 2
                new_wlst = list(str(word))
                new_word = ''.join(list(map(lambda x: str(x).upper(), new_wlst)))
                print(f'upper(map): {str(word)} {str(new_word)}')
            case 'reverse':
                print(f'reverse: {str(word)} {str(word)[::-1]}')
            case 'double':
                print(f'double: {str(word)} {str(word) * 2}')
            case 'del_digits':
                for j in range(len(word)):
                    try:
                        if int(word[j]) not in range(0,9):
                            new_word += str(word[j])
                    except ValueError:
                        new_word += str(word[j])
                print(f'del_digits:  {str(word)}  {str(new_word)}')
            case 'del_even':
                for k in range(len(str(word))):
                    if k%2 == 0:
                        new_word += word[k]
                print(f'del_even:  {str(word)}  {str(new_word)}')
            case 'replace':
                for j in range(len(word)):
                    try:
                        if int(word[j]) in range(0,9):                     
                            new_word += 'Python'
                    except ValueError:
                        new_word += str(word[j])
                print(f'replace:  {str(word)}  {str(new_word)}')

    return 'Операции со строкой выполнены!'

print(help(my_func1))
print(my_func1(text, iv_n_word=n_word, iv_actions=actions))

# 2 task
# полиморфизм: 
# функция len(), например, в зависимости от типа входного параметра выполняет по разному подсчет длины аргумента
my_list = list([1,2,3,4,5])
my_str = str()
my_str = 'Polimorphism'
print(len(my_list))
print(len(my_str))

# инкапсуляция
# может быть реализована через механизм вложенных функций: 
# функция inner_func() защищена и не может быть вызвана напрямую
def outer_func(number):
    # возможна валидация входного значения
    if not isinstance(number, int):
        raise TypeError('Ошибка TypeError!')
    def inner_func():
        return number + 1
    return inner_func()

print(outer_func(999))
# print(inner_func()) - возникнет ошибка при вызове функции

# наследование
# возможно может быть реализовано через передачу имени функции как аргумента в другую функцию,
# тем самым целевая функция как бы наследует ее действия + выполняет другие действия
def calc1_func(x):
    if isinstance(x, int):
        x = x * x
        return x
    else:
        raise TypeError(f'Это не число: {x}')
    

def calc2_func(calc_func, y):
    if callable(calc_func) and isinstance(y, int) and y > 0:
        return math.sqrt(calc_func(y))
    else:
        raise TypeError('Что-то пошло не так!')

print(calc2_func(calc1_func, 4))