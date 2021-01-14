with open('task-6-subjects.txt', encoding='UTF-8') as subject:
    data = {}
    for line in subject:
        line = line.split()
        sum_result = sum([int(x.split('(')[0]) for x in line[1:] if x != '-'])
        data[line[0]] = sum_result
print(data)