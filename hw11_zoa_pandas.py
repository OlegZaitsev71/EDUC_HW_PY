import pandas as pd
import warnings  

warnings.filterwarnings('ignore')
pd.set_option('display.width', 100) 
pd.set_option('display.max_columns', 20)

# Series
temperatures = [22, 25, 19, 30, 24]
days = ["Пн", "Вт", "Ср", "Чт", "Пт"]
temperature_series_named = pd.Series(temperatures, index=days)
print("Series с названиями дней:")
print(temperature_series_named)

# DataFrame 
data = {
    'Имя': ['Анна', 'Борис', 'Виктор', 'Мария'],
    'Возраст': [25, 30, 35, 28],
    'Город': ['Москва', 'Санкт-Петербург', 'Казань', 'Москва']
}

df = pd.DataFrame(data)
print("DataFrame из словаря:")
print(df)
print(f"Тип объекта: {type(df)}")
print()
print("Структура DataFrame:")
print(f"Количество строк, столбцов: {df.shape}")
print(f"Названия столбцов: {df.columns}")
print(f"Индексы строк: {df.index}")

# Задаем кастомные индексы (не числа, а буквы)
# df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

# head(), tail() - выбор числа строк начало/конец

# Выбор по меткам - loc(), iloc()
'''print("1. Строка с индексом 'c':")
print(df.loc['c'])              # строки
print(df.loc['b', 'Имя'])       # ячейки
print(df.loc[['a', 'c'], ['Имя', 'Зарплата']])  # строки + столбцы
print(df.iloc[1:3]) # выбор по номера строк
'''
# Загрузка из файлов
# with open('complex_data.csv', 'w', encoding='utf-8') as f:
#    f.write(complex_data)

complex_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Анна', 'Борис', 'Виктор', 'Мария', 'Ольга'],
    'age': [25, 30, 35, 28, 32],
    'date':['2024-01-01', '' , '2023-02-02', '2022-03-03', '' ]
                }

# pd.DataFrame(complex_data).to_csv('hw11/complex_data.csv', index=False)

'''complex_data1 = pd.read_csv(
    'hw11/complex_data.csv',
    parse_dates=['date'],  # Попытаться распарсить даты
    dayfirst=True,        # Формат месяц/день/год (а не день/месяц/год)
    na_values=[''],        # Пустые строки как NaN
    keep_default_na=True   # Сохранить стандартные значения NaN
)
print("С обработкой дат и пропусков:")
print(complex_data1)'''

# Загрузка с MS EXCEL
df_dirty_loaded = pd.read_excel(
    'hw11/complex_data1.xlsx',
    skiprows=3,        # Пропустить первые 2 строки
    usecols='D:H',     # Только колонки D, E, F, G (id, name, age, salary)
    header=0           # Первая строка - заголовки
)

print("MS EXCEL. После настройки параметров (dirty load):")
print(df_dirty_loaded)
df_cleaned = df_dirty_loaded.copy()
df_cleaned.columns = ['id', 'name', 'age', 'salary', 'join_date']
df_cleaned['age'] = pd.to_numeric(df_cleaned['age'], errors='coerce')
df_cleaned['salary'] = df_cleaned['salary'].fillna(df_cleaned['salary'].mean())
df_cleaned['join_date'] = pd.to_datetime(df_cleaned['join_date'], errors='coerce')

print('MS EXCEL. df_cleaned():')
print(df_cleaned)
#todo