def sum_func(x,y,z):
    """
    Функция принимает 3 числовых значение и вычислияет сумму двух наибольших из трех чисел
    :param var_1: Число_1
    :param var_2: Число_2
    :param var_3: Число_3
    :return: sum(сумма трех чисел) - min(минимальное число)
    """
    return sum([x,y,z]) - min(x,y,z)

num_list = []
for user_number in range(1,4):
    num_list.append(int(input(f'Введите {user_number}-е число: ')))

sum_result = sum_func(num_list[0], num_list[1], num_list[2])
print(sum_result)