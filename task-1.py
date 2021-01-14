with open('str_file.txt', 'w') as str_file:
    while True:
        string = input('Введите строку: ')
        if string == '':
            break
        else:
            print(string, file=str_file)

with open('str_file.txt', 'r') as str_file:
    content = str_file.read()
    print(content)
