class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculation(self, thickness):
        print(f'{int(self.__length * self.__width * 25 * (thickness * 0.01))} т асфальта.')

road = Road(length=2500, width=6)

road.calculation(int(input('Введите толщину в см: ')))

