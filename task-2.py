with open('task-2.txt', 'r') as file:
    words = 0
    for numb, line in enumerate(file, start=1):
        print(f'В {numb}-й строке {len(line.split())} слов. - {line}')
        words = len(line.split()) + words
print(f'\nВ файле {numb} строки и всего {words} слов')
