from abc import ABC, abstractmethod

class AbsClass(ABC):
    @abstractmethod
    def calc1(self):
        print('Абстрактный метод calc1')

    @abstractmethod
    def calc2(self):
        print('Абстрактный метод calc2')

class Clothes(AbsClass):
    def calc1(self):
        print('Абстрактный метод calc1')

    def calc2(self):
        print('Абстрактный метод calc2')

    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        print(f'Общий расход: {self.size + other.size}')


class Coat(Clothes):
    @property
    def calc1(self):
        return f'Расход ткани на пальто: {(self.size / 6.5 + 0.5):.2f}'

class Costume(Clothes):
    @property
    def calc2(self):
        return f'Расход ткани на костюм: {(2 * self.size + 0.3):.2f}'

coat = Coat(size=7)
print(coat.calc1)
costume = Costume(size=5)
print(costume.calc2)
coat + costume
