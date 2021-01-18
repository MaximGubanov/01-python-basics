class Worker:
    def __init__(self, wage, bonus):
        self.name = 'Maxim'
        self.surname = "Gubanov"
        self.position = 'Engineer'
        self.__income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}\nДолжность: {self.position}')

    def get_total_income(self):
        print(f'Доход сотрудника с учётом премии: {sum(dict.values(self._Worker__income))}')

worker = Position(54200, 12000)
worker.get_full_name()
worker.get_total_income()

