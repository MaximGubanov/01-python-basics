class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки...')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}.')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}.')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}.')

p = Stationery(title='')
p.draw()

pen = Pen(title='ручки')
pen.draw()
pencil = Pencil(title='карандаша')
pencil.draw()
handle = Handle(title='маркера')
handle.draw()