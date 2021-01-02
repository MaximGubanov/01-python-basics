import sys
salary, working_days, prize = sys.argv[1:]

def calc_money_func(salary, working_days, prize):
    """
    Расчет ЗП
    prize: Премия
    :param salary: Оклад
    :param working_days: Кол-во отработанных дней
    :return:
    """
    making_money = salary / 20 * working_days
    print(f'Ваш заработок за {working_days} дней составляет {(making_money):.2f} рублей.\n'
          f'Плюс премия {prize} % за отработанные дни составляет {(making_money / 100 * prize):.2f} рублей.\n'
          f'Итого с учетом налога: {((making_money + prize) - (making_money + prize) * 0.13):.2f} рублей')

calc_money_func(int(salary), int(working_days), int(prize))


