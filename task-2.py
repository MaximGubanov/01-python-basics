user_db = []
req = ('Имя', 'Фамилия', 'Возраст', 'Город', 'E-mail', 'Телефон')

def user_database(name, family, age, city, email, mob):
    """"
    Функция принимает введенные данные о пользователе и выводит их на экран
    Name: Имя
    Family: Фамилия
    Age: Возраст
    City: Город
    Email: Эл. почта
    mob: Телефон
    """
    return print(f'Имя: {name}, Фамилия: {family}, Возраст: {age},'
                 f' Город: {city}, e-mail: {email}, тел: {mob}')

for i in req:
    user_db.append(input(f'{i}: '))
user_database(name=user_db[0], family=user_db[1], age=user_db[2], city=user_db[3], email=user_db[4], mob=user_db[5])


