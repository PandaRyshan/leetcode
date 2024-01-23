import asyncio
import aiohttp
import json
import time
import requests


API_KEY = '2c7b6bcb41eb6ddca01ece8ace8bc0e3'
URLs = [
    'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
        .format(lat=39.56, lon=116.20, api_key=API_KEY),
    'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
        .format(lat=35.50, lon=107.92, api_key=API_KEY),
    'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
        .format(lat=23.12, lon=113.28, api_key=API_KEY)
]


def sync_fetch(url):
    response = requests.get(url)
    return response.text


def test_sync():
    for url in URLs:
        response = sync_fetch(url)
        print(response)


async def async_fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        

async def test_async():
    starttime = time.time()

    tasks = [asyncio.create_task(async_fetch(url)) for url in URLs]
    responses = await asyncio.gather(*tasks)
    for response in responses:
        print(response)

    endtime = time.time()
    print('time: ', endtime - starttime)


asyncio.run(test_async())
test_sync()
