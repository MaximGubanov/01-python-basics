def div_func(div_x, div_y):
    """
    Функция принимает два числа и возвращает результат их деления
    :param div_x: Делимое
    :param div_y: Делитель
    :return: div_x / div_y = -> 10 / 5 = 2
    """
    try:
        return div_x / div_y
    except ZeroDivisionError:
        print('Делить на ноль нельзя')

x = int(input('Введите делимое: '))
y = int(input('Введите делитель: '))
user_request = div_func(x, y)
print(f'Результат деления: {user_request}')

