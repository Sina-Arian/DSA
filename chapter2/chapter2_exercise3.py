from random import randint, randrange
from chapter2_exercise2 import Card

'''3.Write a simple implementation of a card deck tto deal cards out randomly ...'''

class Deck:
    def __init__(self):
        self.card_list =[]
        while len(self.card_list) != 52:
            new_card = randint(0,51)
            if new_card in self.card_list:
                continue
            else:
                self.card_list.append(new_card)

    def deal(self):
        number = randrange(len(self.card_list))
        card = self.card_list.pop(number)
        return Card(card)

    def cardLeft(self):
        return len(self.card_list)
