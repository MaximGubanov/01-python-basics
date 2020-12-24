product = None
price = None
quantity = None
new_database = []
result_list = []
i = 1

count_product = int(input('В каком кол-ве пришла продукция: '))

while i <= count_product:
    database = {}
    product = input('Введите название товара: ')
    database['Название'] = product

    price = int(input(f'Введите цену {product}: '))
    database['Цена'] = price

    quantity = int(input('В каком количестве: '))
    database['шт'] = quantity

    new_database.append(i)
    new_database.append(database)

    i += 1

my_tuple = tuple(new_database)
result_list.append(my_tuple)
print(result_list)



