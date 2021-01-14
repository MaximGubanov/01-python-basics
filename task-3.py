all_average_salary, average_salary, i = 0, 0, 0
staff_with_min_salary = []

with open('task-3-list-staff.txt', 'r') as all_staff:
    for num, line in enumerate(all_staff, start=1):
        line = line.split()
        all_average_salary = float(line[1]) + all_average_salary
        if float(line[1]) < 20000:
            staff_with_min_salary.append(line[0])
            average_salary = float(line[1]) + average_salary
            i += 1

print(f'\nСредний оклад всех сотрудников: {(all_average_salary / num):.2f} рублей\n'
      f'Средний оклад {i}-x  сотрудникв с ЗП < 20000 рублей: {(average_salary / i):.2f} рублей,\n'
      f'вот фамилии этих сотрудников: {(", ".join(staff_with_min_salary))}.')
