import requests
from bs4 import BeautifulSoup
import queue
import threading
import json
import openpyxl

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# proxies = {
#     # 'https': 'http://proxy_ip:proxy_port'
#     'https': f'http://{login}:{password}@proxy_ip:proxy_port'
# }

proxies = {
            'https': 'https://148.251.76.237:18080'
            }


def get_location(url):
    response = requests.get(url=url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text, 'lxml')
    
    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value-country').text.strip()
    
    print(f'IP: {ip}\nLocation: {location}')


def main():
    get_location(url='https://2ip.ru')
# https://atomurl.net/myip/
# https://ipinfo.io/ 

#------------------------проверка из файла
# q = queue.Queue()
# Valid_proxy = []

# with open('proxy_list.txt', 'r') as f:
#     proxies = f.read().split('\n')
#     for p in proxies:
#         q.put(p)


# def check_proxy():
#     global g
#     while not q.empty():
#         proxy = q.get()
#         try:
#             res = requests.get('https://ipinfo.io/json', proxies={'https': proxy}, timeout=5)
#             print(str(res.status_code) + ' | ' + str(proxy))
#         except:
#             continue
#         if res.status_code == 200:
#             print(str(res.status_code) + ' | ' + str(proxy))
#             # print(proxy)

# for _ in range(10):
#     threading.Thread(target=check_proxy).start()
#-----------------------

# читаем json файл data.json' и выводим в цикле все даныные из "data": {"products"



# Создаем новый Excel файл
# wb = openpyxl.Workbook()
# ws = wb.active
# # Заголовки столбцов
# ws.append(['Article ID', 'Brand', 'Name', 'Price'])

# # Открываем файл pars_json.json
# pars_json =  r'C:/Users/Илья/Desktop/wildberries_parser/wildberries_parser/pars_json.json'
# with open(pars_json, encoding='utf-8') as f:
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
#         ws.append([article_id, brand, name, price])

# # Сохраняем файл
# wb.save('output.xlsx')


input_string = '12345600'
def add_commas(input_string):
    """Функция добавления зяпятой после двух послдених символов"""
    x= int(len(input_string)-2)
    print(input_string[:x] +','+ input_string[x:])
    print()

add_commas(input_string)





# if __name__ == '__main__':
#     main()
#     check_proxy()
