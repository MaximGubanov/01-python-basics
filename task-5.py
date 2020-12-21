proceeds = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))

if proceeds > costs:
    profit = proceeds - costs
    print(f"Ваша фирма в прибыли и она составляет {profit} рублей.")
    profitability = (profit / costs) * 100
    print(f"Рентабельность фирмы {profitability:.0f}%.")
    staff = int(input('Сколько сотрудников в вашей фирме? '))
    print(f"Прибыль в рассчете на одного сотрудника составляет - {(profit / staff):.2f} рублей.")
else:
    print('Ваша фирма в убытке. Наймите хорошего маркетолога.')