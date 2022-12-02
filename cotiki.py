import random
from random import randint
from cat import Cat
class Cotiki(Cat):
    def __init__(self,name,parent):
        super().__init__(name)
        self.parent = parent
    def __str__(self):
        return super().__str__() + self.name + ' говорит:' + ' Имя моей мамочки - ' + self.parent