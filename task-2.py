# database_list = ['book',45.7, 458, True, None, 'spoon']
data_base = []
user = None
while True:
    user = input('Создайте список, для завершения введите "q": ')
    if user == 'q':
        print('Список готов.')
        break
    else:
        data_base.append(user)

i = 0
while i < len(data_base):
    if len(data_base) % 2 == 0:
        el_1, el_2 = data_base[i], data_base[i + 1]
        el_1, el_2 = el_2, el_1
        print(el_1, el_2)
        i += 2
    else:
        end_elemenent = data_base.pop()
        continue