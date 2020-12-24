my_list = []
user_number = None

while True:
    user_number = input('Введите значение, нажмите "q" для завершения: ')
    if user_number == 'q':
        break
    else:
        my_list.append(int(user_number))
        my_list.sort()
        my_list.reverse()

print(my_list)


