# -*- coding: utf-8 -*-
# Стартовый файл для теста git

import requests
import json
from query_settings import url, proxies, headers # импортируем настройки запроса. 
prs_json = r'C:/Users/Илья/Desktop/wildberries_parser/wildberries_parser/data.json'

def main(url, proxies, headers): #url, proxies, headers
    response = requests.post(url, proxies=proxies, headers=headers)
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

article_id = (123837569,210087382)


def num_basket(article_id):
    """Функция для формирования url в зависимости от артикула"""
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
        
        return basket


if __name__ == '__main__':
    # main(url, proxies, headers) #url, proxies, headers
    num_basket(article_id)