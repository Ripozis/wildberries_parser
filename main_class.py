# -*- coding: utf-8 -*-
# Клас для основых функций парсера
import asyncio
import aiohttp
from query_settings import url, proxies, headers # импортируем настройки запроса. 


class WB_parser:
    def __init__(self, url, proxies, headers):
        self.url = url
        self.proxies = proxies
        self.headers = headers

    async def requests_cat(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=self.headers) as response: # внести proxy="http://proxy.com"
                data = await response.json()

                for item in data['data']['products']:
                    print('----------------------------------')
                    article_id = item['id']
                    brand = item['brand']
                    name = item['name']
                    price = item['sizes'][0]['price']['total']

                    print(f'Бренд: {brand}')
                    print(f'Название: {name}')
                    print(f'Артикул: {article_id}')
                    print(f'Цена: {price}')

        return data['data']['products']

async def start_class(url, proxies, headers):
    obj = WB_parser(url, proxies, headers)
    result = await obj.requests_cat()
    print(result)

asyncio.run(start_class(url, proxies, headers))