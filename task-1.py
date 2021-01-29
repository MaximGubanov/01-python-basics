import random

class LotoCard:
    def __init__(self, card):
        line = random.sample(range(1, 91), 15)
        self.card = card
        self.line1 = line[:5] + [' ' for _ in range(1, 5)]
        self.line2 = line[5:10] + [' ' for _ in range(1, 5)]
        self.line3 = line[10:15] + [' ' for _ in range(1, 5)]
        random.shuffle(self.line1)
        random.shuffle(self.line2)
        random.shuffle(self.line3)
        self.result = [LotoCard.line_sort(self.line1),
                       LotoCard.line_sort(self.line2),
                       LotoCard.line_sort(self.line3)]

    def __str__(self):
        return '{}{}{}'.format('\t'.join(map(str, line_sort(self.line1)))+'\n'
                               '\t'.join(map(str, line_sort(self.line2)))+'\n'
                               '\t'.join(map(str, line_sort(self.line3)))+'\n')

    @staticmethod
    def line_sort(line):
        temp_line = []
        for i in range(len(line)):
            if line[i] != ' ':
                temp_line.append(line[i])
                line[i] = '&'
        temp_line.sort(reverse=True)
        for i in range(len(line)):
            if line[i] == '&':
                line[i] = temp_line.pop()
        return line

class LotoGame:
    def __init__(self, human_player, human_name, computer_player):
        self.card1 = human_player
        self.human_name = human_name
        self.card2 = computer_player
        num_list = [x for x in range(1, 91)]
        random.shuffle(num_list)
        self.rand_list = num_list

    def start(self):
        while True:
            print(f'-------------Карточка {self.human_name}-------------')
            for i in range(len(self.card1)):
                print('{}'.format('\t'.join(map(str, self.card1[i]))))
            print('-----------Карточка компьютера-----------')
            for i in range(len(self.card2)):
                print('{}'.format('\t'.join(map(str, self.card1[i]))))

            rand_number = self.rand_list.pop()
            print(f'Выпал бочонок: {rand_number}, в мешке осталось {len(self.rand_list)}')
            answer = input('Хотите зачеркнуть ? (y/n): ')

            self.card2 = [['-' if el == rand_number else el for el in self.card2[i]]
                          for i in range(len(self.card2))]
            if not any(isinstance(i, int) for i in [i for line in self.card1 for i in line]):
                print('Игра завершена. Вы выиграли!')
                break
            elif not any(isinstance(i, int) for i in [i for line in self.card1 for i in line]):
                print('Игра завершена. Победил компьютер!')
                break
            elif answer == 'y' and any(rand_number in i for i in (self.card1[j] for j in range(len(self.card1)))):
                self.card1 = [['-' if el == rand_number else el for el in self.card1[i]]
                              for i in range(len(self.card1))]
            elif answer == 'n' and not any(rand_number in i for i in (self.card1[j] for j in range(len(self.card1)))):
                continue
            else:
                print('Игрок ввел не верно')
                break

human_player = LotoCard('Игрок')
computer_player = LotoCard('Копьютер')

game = LotoGame(human_player.result, human_player.card, computer_player.result)
game.start()



