import random
from random import randint
class Cat:
    def __init__(self, name): #
        self.name = name #присваивание имя
        self.answers = ['Муррр', 'Мяяяууу'] #ответы
        self.number = [0, 0] #счётчик ответов

    def to_answer(self):
        answer = random.choice(self.answers) #генерирует рандомный ответ
        self.number[self.answers.index(answer)] += 1 #по идее должен суммировать количество ответов данного индекса
        print(self.name + ' говорит: ' + answer) #вывод на экран ответ
        return self.number

    def __str__(self):
        x = ''
        for index in range(len(self.answers)):
            x += str(self.name) + ' сказала ' + str(self.answers[index]) + ' ' + str(self.number[index]) + ' раз' + '\n' #вывод на экран
        return x