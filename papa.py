import random
from random import randint
import random
from random import randint
class Papa:
    def __init__(self, name):
        self.name = name
        self.answers = ['Иди кушать','Слушайся маму','Помой посуду','Дышать темно и воздуха не видно']
        self.number = [0, 0, 0, 0]

    def to_answer(self):
        answer = random.choice(self.answers)  # генерирует рандомный ответ
        self.number[self.answers.index(answer)] += 1  # по идее должен суммировать количество ответов данного индекса
        print(self.name + ' говорит: ' + answer)  # вывод на экран ответ
        return self.number

    def __str__(self):
        x = ''
        for index in range(len(self.answers)):
            x += str(self.name) + ' сказала ' + str(self.answers[index]) + ' ' + str(
                self.number[index]) + ' раз' + '\n'  # вывод на экран
        return x