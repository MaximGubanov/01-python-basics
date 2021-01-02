original_list = [17, 2, 6, 5, 4, 8, 3, 11, 13, 5, 4, 7, 8, 9, 2]
gen_list = [i for i in original_list if i > original_list[original_list.index(i) - 1]]

print(f'Исходный лист: {original_list}\nНовый: {gen_list}')
