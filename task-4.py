my_set = [1, 2, 2, 2, 4, 23, 11, 11, 11, 27, 45, 76, 54, 76, 4, 2, 165, 12, 11, 234, 45]
new_list = [i for i in my_set if my_set.count(i) == 1]
print(f'Исходное множество: {my_set}\nРезультат: {new_list}')