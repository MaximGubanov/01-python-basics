from itertools import cycle
numb_list = ['Ubuntu', 'Mint', 'CentOS', 'Debian', 'Manjaro', 'Kubuntu', 'RadHat', 'KDENeon']

def iter_func(c):
    iter = 0
    for i in cycle(numb_list):
        if iter == c:
            return print('\nStop')
        else:
            print(i)
            iter += 1

iter_func(int(input('Введите число итераций: ')))