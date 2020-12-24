dict_saesons = {
    'зимний': [12, 1, 2],
    'весенний': [3, 4, 5],
    'летний': [6, 7, 8],
    'осенний': [9, 10, 11]
}

list_months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
               'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')

month = int(input('Ведите порядковый номер месяца: '))
for season in dict_saesons.keys():
    if month in dict_saesons.get(season):
        print(f'{list_months[month - 1]} - это {season} месяц.')