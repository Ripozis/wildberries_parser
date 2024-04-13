# -*- coding: utf-8 -*-
# Клас для основых функций парсера
import asyncio
import aiohttp
from query_settings import url, proxies, headers # импортируем настройки запроса. 
import openpyxl
import json
import math


class WB_parser:
    def __init__(self, url, proxies, headers):
        self.url = url
        self.proxies = proxies
        self.headers = headers

    async def requests_url(self) -> dict:
        """Функция запроса данных по url"""
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.url, proxy=self.proxies) as response:
                data = await response.json()
                return data
    
    def num_basket(article_id):
        """Функция для формирования url товара в зависимости от артикула"""
        for product in article_id:
            vol_id = int(product)//100000 
            part = str(product)[:6]
            vol = str(product)[:4]

            print(vol_id)
            if 0 <=vol_id<= 143:
                basket = "01"
            elif 144 <=vol_id<= 287:
                basket = "02"
            elif 288 <=vol_id<= 431:
                basket = "03"
            elif 432 <=vol_id<= 719:
                basket = "04"
            elif 720 <=vol_id<= 1007:
                basket = "05"
            elif 1008 <=vol_id<= 1061:
                basket = "06"
            elif 1062 <=vol_id<= 1115:
                basket = "07"
            elif 1116 <=vol_id<= 1169:
                basket = "08"
            elif 1170 <=vol_id<= 1313:
                basket = "09"
            elif 1314 <=vol_id<= 1601:
                basket = "10"
            elif 1602 <=vol_id<= 1655:
                basket = "11"
            elif 1656 <=vol_id<= 1919:
                basket = "12"
            elif 1920 <=vol_id<= 2045:
                basket = "13"
            elif 2046 <=vol_id<= 2189:
                basket = "14"
            elif 2091 <=vol_id<= 2405:
                basket = "15"
            else:
                basket = "16"
        
        url = f'https://basket-{basket}.wbbasket.ru/vol{vol}/part{part}/{product}/info/ru/card.json'
        print(url)
        return url


    def increment_page_if_products_exist(url):
        """Функция для увеличения значения page на 1 в ссылке, если "products" не пустой"""
        # Выполняем GET-запрос к указанной ссылке
        # url_seller_art_count = 'https://catalog.wb.ru/sellers/v4/filters?appType=1&curr=rub&dest=12358048&filters=xsubject&spp=30&supplier=39232&uclusters=1'
        url_catalog_art_count = 'https://catalog.wb.ru/catalog/stationery4/v4/filters?appType=1&curr=rub&dest=12358048&spp=30&subject=4570&uclusters=0'
        seller_art_count = asyncio.run(start_class(url_catalog_art_count, proxies, headers))  # напиши код для получения результата запроса из requests_url() 
        art_count = math.ceil((seller_art_count.json()["data"]["total"])/100)  # получаем общее количество страниц для цикла
        # print(art_count)

        for i in range(art_count):

            # Получаем текущее значение page из URL
            """url.split('?')[-1]: Разделяет URL на части по символу ? и выбирает последнюю часть, которая 
            содержит параметры запроса после знака вопроса.
            url.split('?')[-1].split('&'): Разделяет последнюю часть URL на подстроки, используя символ & в 
            качестве разделителя, чтобы получить отдельные параметры.
            p.split('=') for p in ...: Проходится по каждой из этих подстрок и разделяет их по символу = для 
            создания пар ключ-значение.
            dict(...): Создает словарь, используя полученные пары ключ-значение."""
            params = dict(p.split('=') for p in url.split('?')[-1].split('&'))
            # page = int(params['page'])

            # Добавляем 1 к значению page
            i += 1
    
            # Обновляем значение page в URL
            params['page'] = str(i)

            # Собираем обновленный URL
            """url.split('?')[0]: Разделяет исходный URL на две части по символу ? и выбирает первую часть, 
            которая содержит базовый адрес без параметров.
            + '?': Добавляет к базовому адресу знак вопроса, чтобы начать список параметров запроса.
            '&'.join(...): Преобразует словарь params обратно в строку параметров запроса, соединяя каждую пару 
            ключ-значение символом &.
            [f"{k}={v}" for k, v in params.items()]: Проходится по каждой паре ключ-значение в словаре params и 
            формирует строку вида "ключ=значение" для каждой пары."""
            updated_url = url.split('?')[0] + '?' + '&'.join([f"{k}={v}" for k, v in params.items()])
            print(updated_url)
            # Ссылка для тестирования👆
            #_seller_art
            # url = "https://catalog.wb.ru/sellers/v2/catalog?appType=1&curr=rub&dest=12358048&page=19&sort=popular&spp=30&supplier=39232&uclusters=1"
            url = "https://catalog.wb.ru/catalog/stationery4/v2/catalog?appType=1&curr=rub&dest=12358048&page=1&sort=popular&spp=30&subject=4570&uclusters=0"
            url = "https://catalog.wb.ru/catalog/stationery4/v2/catalog?appType=1&cat=130944&curr=rub&dest=12358048&sort=popular&spp=30&uclusters=0"

    def pars_response(response_json):
            """Функция для разбора json"""
            data = (response_json)['data']['products']
            for item in data:
                    print('----------------------------------', end='\n')
                    article_id = item['id']
                    brand = item['brand']
                    name = item['name']
                    price = item['sizes'][0]['price']['total']
                    print(f'Бренд: {item["brand"]}')
                    print(f'Название: {item["name"]}')
                    print(f'Артикул: {item["id"]}')
                    print(f'цена: {price}')


    def add_commas_price(input_price):
            """Функция добавления зяпятой после двух послдених символов"""
            x= int(len(input_price)-2)
            print(input_price[:x] +','+ input_price[x:])
            
            
    def save_file(data):
        """Функция для сохранения в Excel файл"""
        # Создаем новый 
        wb = openpyxl.Workbook()
        ws = wb.active
        # Заголовки столбцов
        ws.append(['Article ID', 'Brand', 'Name', 'Price'])
        # Получать уже готовый словарь?
        data = (json.load(data))['data']['products']
        for item in data: 
            print('----------------------------------', end='\n')
            article_id = item['id']
            brand = item['brand']
            name = item['name']
            price = item['sizes'][0]['price']['total']
            print(f'Бренд: {item["brand"]}')
            print(f'Название: {item["name"]}')
            print(f'Артикул: {item["id"]}')
            print(f'цена: {price}')
            ws.append([article_id, brand, name, price])



async def start_class(url, proxies, headers):
    obj = WB_parser(url, proxies, headers)
    result = await obj.requests_url()
    print(result)

asyncio.run(start_class(url, proxies, headers))