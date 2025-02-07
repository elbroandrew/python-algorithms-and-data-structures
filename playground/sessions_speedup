'''
Sessions are always speedup multiple requests
'''

import requests
import httpx
import aiohttp
import asyncio
import time
from functools import wraps


URL = 'https://jsonplaceholder.typicode.com/posts/1'

n = 10
 
def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        begin = time.perf_counter()
        result = f()
        end = time.perf_counter()
        print(f"{f.__name__}: ВРЕМЯ: {end - begin} секунд для {n} запросов")

        return result
    return wrap


def requests_with_session(session: requests.Session):
    resp = session.get(f"{URL}")
    return resp.json()


def request_no_session():
    resp = requests.get(f"{URL}")
    return resp.json()


@timing
def main():
    for _ in range(n):
        request_no_session()
        
    
# main()   # ВРЕМЯ: 4.0919731 секунд для 10 запросов


@timing
def main2():
    with requests.Session() as s:
        for _ in range(n):
            requests_with_session(s)
    
# main2()  #  ВРЕМЯ: 1.4663715 секунд для 10 запросов


def httpx_no_session():
    resp = httpx.get(URL)
    return resp.json()

def httpx_with_sync_session(c: httpx.Client):
    resp = c.get(URL)
    return resp.json()

@timing
def main3():
    for _ in range(n):
        httpx_no_session()

    
# main3() #  ВРЕМЯ: 4.340639 секунд для 10 запросов

@timing
def main4():
    with httpx.Client() as c:
        for _ in range(n):
            httpx_with_sync_session(c)
        
    
# main4() #  ВРЕМЯ: 1.6302089000000002 секунд для 10 запросов


async def httpx_with_async_client(c: httpx.AsyncClient):
    resp = await c.get(URL)
    return resp.json()

async def main5():
    begin = time.perf_counter()
    async with httpx.AsyncClient() as c:
        tasks = [httpx_with_async_client(c) for _ in range(n)]
        results = await asyncio.gather(*tasks)
        
    end = time.perf_counter()
    print(f"ВРЕМЯ: {end - begin} секунд для {n} запросов")

#asyncio.run(main5())  # ВРЕМЯ: 0.7983056000000001 секунд для 10 запросов


async def aiohttp_async_with_session(session: aiohttp.ClientSession):
    async with session.get(URL) as resp:
        return await resp.json()
    
async def main():
    begin = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        # await aiohttp_async_with_session(session)
        loop = asyncio.get_event_loop()
        tasks = [loop.create_task(aiohttp_async_with_session(session)) for _ in range(n)]
        results = await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f"ВРЕМЯ: {end - begin} секунд для {n} запросов")

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # for Windows: RuntimeError: Event loop is closed
asyncio.run(main())  #  ВРЕМЯ: 0.561911 секунд для 10 запросов
        