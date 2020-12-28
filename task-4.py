def exp_func(x, y):
    """
    Функция возводит X в степень Y и возвращает результат возведения.
    :param x: любое натуральное число (например 2)
    :param y: степень положительная или отрицательная (например 3 или -3)
    :return: x ** y = 2 ** 3 = 8;
    или
    :return: x ** (-y) = 1 / (x ** y) = 1 / (2 ** 2) = 0,125;
    или
    :return x ** 0 = 1
    """
    exp = 1
    if y < 0:
        for i in range(abs(y)): exp = exp * x
        return 1 / exp
    elif y >= 0:
        return x ** y

x = int(input('Введите любое натуральное число "x": '))
y = int(input('Введите степень для "x" со знаком "+" или "-": '))
print(f'Результат возведения {x} в степень {y} равно {exp_func(x, y)}')