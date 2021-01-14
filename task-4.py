list_ru = ['Один', 'Два', 'Три', 'Четыре']
ru = []

with open('task-4-EN-replacement.txt') as en_file:
    en = en_file.readlines()
    for num, x in enumerate(en):
        x = x.split()
        x[0] = list_ru[num]
        ru.append(x[0])

with open('task-4-RU-replacement.txt', 'w', encoding='UTF-8') as ru_file:
    for num, x in enumerate(ru, 1):
        ru_file.write('{} - {}\n'.format(x, num))
