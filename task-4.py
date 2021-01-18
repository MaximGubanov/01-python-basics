class Car:
    def __init__(self, name, speed, color):
        is_police = bool()
        self.name = name
        self.speed = speed
        self.color = color

    def go(self):
        print('Машина поехала...')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print(f'Повернули на {direction}...')

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили скорость! Ваша скорость > {self.speed} км\ч'
        else:
            return f'Ваша скорость: {self.speed} км\ч'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость! Ваша скорость > {self.speed} км\ч'
        else:
            return f'Ваша скорость: {self.speed} км\ч'

class PoliceCar(Car):
    pass

auto_town = TownCar(name='Mazda', speed=59, color='Синий')
print(f'Название: {auto_town.name}\nЦвет: {auto_town.color}\n'
      f'{auto_town.show_speed()}')
auto_town.go()
auto_town.turn(direction='лево')
auto_town.stop()

auto_work = WorkCar(name='Audi', speed=41, color='Серебристый')
print(f'\n\nНазвание: {auto_work.name}\nЦвет: {auto_work.color}\n'
      f'{auto_work.show_speed()}')
auto_town.go()
auto_town.turn(direction='право')
auto_town.stop()