my_list = []
new_list = []
element = None
last_element = None
i = 0

while True:
    element = input('Создайте список, по окончании нажмите "q": ')
    if element == 'q':
        print('Список готов.')
        break
    else:
        my_list.append(element)

while i < len(my_list):
    if len(my_list) % 2 == 1:
        last_element = my_list.pop()
        continue
    else:
        el_1, el_2 = my_list[i], my_list[i + 1]
        el_1, el_2 = el_2, el_1
        new_list.append(el_1)
        new_list.append(el_2)
        i += 2

if last_element:
    new_list.append(last_element)

print(f"{my_list} - {new_list}")