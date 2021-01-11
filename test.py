from mock_data import tours, departures

def get_name_departures(data):
    '''
    Данная функция возвращает названия всех городов без предлога "Из"
    '''
    new_data = {}
    for key, val in data.items():
        dep = val.split(' ')[1]
        temp_data = new_data.fromkeys([key], dep)
        new_data.update(temp_data)
    return new_data


dep = get_name_departures(departures)

print(dep)
print(dep['msk'])
