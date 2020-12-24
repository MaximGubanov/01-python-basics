user_string = input('Введите строку через пробел: ')

user_string = user_string.split()

print(f'Это полная строка: {user_string}')

for i, element in enumerate(user_string, 1):
    print(f'{i} - {element[:10]}')