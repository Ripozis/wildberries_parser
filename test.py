import requests
from query_settings import  proxies, headers # импортируем настройки запроса. 
import math


def increment_page_if_products_exist(url):
    """Функция для увеличения значения page на 1 в ссылке, если "products" не пустой"""
    # Выполняем GET-запрос к указанной ссылке
    # url_seller_art_count = 'https://catalog.wb.ru/sellers/v4/filters?appType=1&curr=rub&dest=12358048&filters=xsubject&spp=30&supplier=39232&uclusters=1'
    url_catalog_art_count = 'https://catalog.wb.ru/catalog/stationery4/v4/filters?appType=1&curr=rub&dest=12358048&spp=30&subject=4570&uclusters=0'
    
    
    seller_art_count = requests.get(url_catalog_art_count, proxies=proxies, headers=headers)
    art_count = math.ceil((seller_art_count.json()["data"]["total"])/100)  # получаем количество страниц 
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
        list_url = []
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
        list_url.append(updated_url)
        print(updated_url)
        #добавление в список данных через цикл 


# Ссылка для тестирования
#_seller_art
# url = "https://catalog.wb.ru/sellers/v2/catalog?appType=1&curr=rub&dest=12358048&page=19&sort=popular&spp=30&supplier=39232&uclusters=1"
url = "https://catalog.wb.ru/catalog/stationery4/v2/catalog?appType=1&curr=rub&dest=12358048&page=1&sort=popular&spp=30&subject=4570&uclusters=0"
url = "https://catalog.wb.ru/catalog/stationery4/v2/catalog?appType=1&cat=130944&curr=rub&dest=12358048&sort=popular&spp=30&uclusters=0"
# Получаем обновленный URL с увеличенным значением page, если "products" не пустой
# updated_url = increment_page_if_products_exist(url)
# print("Обновленный URL:", updated_url)

# добавление в список данных через цикл