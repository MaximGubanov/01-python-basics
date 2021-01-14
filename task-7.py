import json

with open('task-7-enterprises.txt') as enterprises:
    profit, damages_profit, averages_profit = {}, {}, {}
    result_list = []
    sum_profit, sum_damages = 0, 0

    for line in enterprises:
        line = line.split()
        profit_res = int(line[2]) - int(line[3])
        if profit_res > 0:
            profit[line[0]] = profit_res
            sum_profit += profit_res
        else:
            sum_damages += profit_res
            damages_profit['Damages_profit'] = sum_damages

    averages_profit['Averages_profit'] = sum_profit
    result_list.append(profit)
    result_list.append(averages_profit)
    result_list.append(damages_profit)

with open('task-7-enterprises.json', 'w') as file_json:
    json.dump(result_list, file_json)









# damages

# profit прибыль
# average_profit
# proceeds выручка
# costs издержки