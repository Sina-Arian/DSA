import sys
sys.path.insert(0, r'C:\Users\Sina\Documents\DSA_Zelle\chapter2')
from chapter2_Card import Card

from random import randrange, randint, shuffle

'''8.Implement an extended Deck class with operations suitable for '''

class Deck():
    def __init__(self):
        cards = []
        for suit in Card._SUITS:
            for rank in Card._RANKS:
                cards.append(Card(rank,suit))
        self.cards = cards

    def size(self):
        return len(self.cards)

    def deal(self):
        return self.cards.pop()

    def shuffleInPlace(self):
        n = self.size()
        cards = self.cards
        for i,card in enumerate(cards):
            pos = randrange(i,n)
            cards[i] = cards[pos]
            cards[pos] = card

    def randomCard(self):
        n = self.size()
        x = randint(0, n)
        return self.cards.pop(x)
    
    def addTop(self, card):
        self.cards.insert(0, card)
    
    def addBottom(self, card):
        self.cards.append(card)

    def addRandom(self, card):
        ind = randint(0, 52)
        self.cards.insert(ind, card)

    def shuffleRandom(self):
        shuffle(self.cards)