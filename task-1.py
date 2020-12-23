database_list = ['book', 458, True, None, 'spoon', False, [1,2,3,5,5], dict(name = 'John')]
i = 0
while len(database_list):
    print(f"{database_list[i]} - {type(database_list[i])}")
    i += 1