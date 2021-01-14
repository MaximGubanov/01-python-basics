with open('numb_file.txt', 'w') as numb_f:
    numbers = input('Введите числа через пробел: ')
    numb_f.writelines(numbers)

try:
    with open('numb_file.txt', 'r') as sum_numbers:
        sum_numbers = sum_numbers.readline()
        sum_numbers = sum_numbers.split()
        print(sum([int(x) for x in sum_numbers]))
except ValueError:
    print('Нужно ввести числа через пробел.')