from itertools import count

for i in count(int(input('Начать с: '))):
    if i > 30: break
    else: print(i, end=' ')

