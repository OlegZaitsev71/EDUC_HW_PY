"""ДЗ №8 по теме <Работа с модулем asyncio в Python>."""  
import requests
import time
from pathlib import Path
import string
import random
import aiohttp
import aiofiles
import asyncio

def gen_random_chars(num_char):
    alpha = string.ascii_uppercase + string.digits
    chars = ''.join(random.choice(alpha) for _ in range(num_char))
    return chars

def gen_name(prefix):
    return prefix + gen_random_chars(4) + '.jpg'

URL = 'https://loremflickr.com/1280/720/kittens'
hw8_zoa_folder = './hw8_zoa_folder'

# Проверка наличия папки
if not Path(hw8_zoa_folder).exists:
    raise FileNotFoundError(f'Папка {hw8_zoa_folder} не найдена!')

path = Path(hw8_zoa_folder).absolute()

# Чтение файлов по URL с использованием модуля requests
start_time = time.time() 
for _ in range(1, 6):
    try:
        r = requests.get(URL, verify=False) 
        file_name = gen_name('1_kittens')
        file_join_path = path.joinpath(file_name)
        file_name_full = Path(file_join_path)
        with file_name_full.open(mode='wb') as f:  
            f.write(r.content)
    except Exception as e:  
        print(f'Что-то пошло не так: {e}') 

end_time = time.time()  
execution_time = end_time - start_time 
print(f'Время requests.get чтения файлов по URL: {execution_time}')

# асинхронный выриант запуска
async def async_gen_random_chars(num_char):
    alpha = string.ascii_uppercase + string.digits
    chars = ''.join(random.choice(alpha) for _ in range(num_char))
    return chars

async def async_gen_name(prefix):
    random_char = await async_gen_random_chars(4)
    return prefix + random_char + '.jpg'

async def fetch_url():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response: 
            return await response.content.read()
        
async def async_generator(): 
    for _ in range(1, 6):
        file_content = await fetch_url()
        yield file_content

async def main():
    async for value in async_generator():  
        file_name = await async_gen_name('2_kittens')
        file_join_path = path.joinpath(file_name)
        file_name_full = Path(file_join_path)
        async with aiofiles.open(file_name_full, 'wb') as f:  
            await f.write(value) 

start_time = time.time()
asyncio.run(main())
end_time = time.time()  
execution_time = end_time - start_time 
print(f'Время asyncio чтения файлов по URL: {execution_time}')

