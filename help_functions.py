'''
Здесь размещаются вспомогательные функции, нужные для предобработки/валидации данных перед передачей в шаблоны
'''

from random import choice


# 1. Получем несколько случаных туров для главной страницы
def max_six_random_items(data):
    '''
    Данная функция извлекает до 6 случайных значений из списка, нужна для работы функции get_tours_for_main

    :param data: список с id туров
    :return: список с 6ю случайными значениями
    '''
    if len(data) >= 6:
        counter = 6
    else:
        counter = len(data)

    new_key_data = []
    for i in range(counter):
        choice_data = choice(data)
        new_key_data.append(choice_data)
        data.remove(choice_data)

    return new_key_data



def get_tours_for_main(data):
    '''
    При помощи get_tours_for_main извлекает 6 случайных туров переменной tours

    :param data: словарь tours с набором туров
    :return: 6 случайных туров в таком же по структуре словаре
    '''
    key_data = data.keys()
    key_data = list(key_data)
    random_items = max_six_random_items(key_data)
    new_data = {}
    for i in random_items:
        temp_data = new_data.fromkeys([i], data[i])
        new_data.update(temp_data)

    return new_data

# 2. Получем туры по месту отправления

def get_name_departures(data):
    '''
    Убирает из названия всех городов предлог "Из", что бы красивее подставлять в UI :)

    :param data: словарь departures
    :return: такойже словарь, только без "Из"
    '''
    new_data = {}
    for key, val in data.items():
        dep = val.split(' ')[1]
        temp_data = new_data.fromkeys([key], dep)
        new_data.update(temp_data)
    return new_data


def get_tours_departure(data, departure):
    '''
    Фильтрует словарь туров по месту отправления

    :param data: словарь tours
    :param departure: код места отправки
    :return: отфильтрованный словарь туров
    '''
    new_data = {}
    for key, val  in data.items():
        if val['departure'] == departure:
            temp_data = new_data.fromkeys([key], data[key])
            new_data.update(temp_data)

    return new_data


def get_nights(data):
    '''
    Извлекает количество ночей из словаря с турами

    :param data: словарь с турами
    :return: список со значениями количества ночей
    '''
    nights = []
    for i in data.values():
        nights.append(i['nights'])

    return nights

def get_prices(data):
    '''
    Извлекает набор цен из словаря туров

    :param data: словарь с турами
    :return: список со значениями цен
    '''
    prices = []
    for i in data.values():
        prices.append(i['price'])

    return prices