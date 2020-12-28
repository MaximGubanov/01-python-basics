def sum_func(s, count_sum):
    """
    Функция принимает числовую строку, преобразует ее в список из чисел и суммирует их на каждом этапе цикла,
    прибавляя предыдущий результат цикла. Выход из программы осуществляется путем введения какого-либо символа
    в конец строки.
    :param s: строка, введення пользователем из последовательности чисел.
    :param count_sum: переменная, которая запоминает результат цикла (сумма чисел одного цикла)
    :return: возвращает итоговый результат полученных сумм каждого цикла
    """
    while True:
        sum_list = []
        split_list = s.split()
        try:
            for i in split_list:
                sum_list.append(int(i))
            count_sum = sum(sum_list) + count_sum
            print(count_sum)
            s = input('Введите числа через пробел: ')
            return sum_func(s, count_sum)
        except ValueError:
            return sum(sum_list) + count_sum

sum_result = sum_func(input(f'Введите числа через пробел\nДля выхода из программы введите любой символ: '), count_sum=0)

print(f'Вы вышли из программы\nРезультат - {sum_result}')

