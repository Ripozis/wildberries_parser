# -*- coding: utf-8 -*-

import requests
import json
from query_settings import url, proxies, headers # импортируем настройки запроса. 
from main_class import WB_parser
import asyncio
import aiohttp


prs_json = r'C:/Users/Илья/Desktop/wildberries_parser/wildberries_parser/data.json'

url_seller = 'https://www.wildberries.ru/seller/89610'

def main(url, proxies, headers): #url, proxies, headers
    response = requests.get(url, proxies=proxies, headers=headers)
    print('Response HTTP Status Code: ', response.status_code)
    #полученые данные переводим в json
    response_json = response.json()
    # полученные данные сохранить в json файл
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)

    # читаем json файл data.json' и выводим в цикле все даныные из "data": {"products"
    # with open(prs_json, encoding='utf-8') as f:
    #     data = (json.load(f))['data']['products']
    #     for item in data: 
    #         print('----------------------------------', end='\n')
    #         article_id = item['id']
    #         brand = item['brand']
    #         name = item['name']
    #         price = item['sizes'][0]['price']['total']
    #         print(f'Бренд: {item["brand"]}')
    #         print(f'Название: {item["name"]}')
    #         print(f'Артикул: {item["id"]}')
    #         print(f'цена: {price}')
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

# value_search = url_seller.split('/')[3]


# if value_search == 'seller':
#     print('seller')
#     seller = url_seller.split('/')[4]
#     print(seller)
# else:
#     print('not seller')

obj = WB_parser(url, headers)
# result = obj.increment_page_if_products_exist(url_seller, seller)

result = asyncio.run(obj.increment_page_if_products_exist(url_seller))
print(result)

if __name__ == '__main__':
    main(url, proxies, headers) #url, proxies, headers


