day = int(input('Сколько спортсмен пробежал киллометров в 1-й день? '))
result = int(input('Каким должен быть его минимальный результат? '))
i = 1
while True:
    print(f"{i}-й день: {day:.2f} км")
    day = day + (day / 100) * 10
    if day > result:
        print(f"{i}-й день: {day:.2f} км")
        break
    i += 1