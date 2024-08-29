import sys
sys.path.insert(0, r'C:\Users\Sina\Documents\DSA_Zelle\chapter2')
from chapter2_Card import Card

from random import randrange
from Deck_Hand import Deck
from time import time

'''1.Modify the Deck class to keep track of the current size of the deck using ...'''

class Deck1():
    _size = 52

    def __init__(self):
        cards = []
        for suit in Card._SUITS:
            for rank in Card._RANKS:
                cards.append(Card(rank,suit))
        self.cards = cards

    def size(self):
        return self._size

    def deal(self):
        self._size -= 1
        return self.cards.pop()

    def shuffle(self):
        n = self.size()
        cards = self.cards
        for i,card in enumerate(cards):
            pos = randrange(i,n)
            cards[i] = cards[pos]
            cards[pos] = card

myDeck1 = Deck1()
myDeck = Deck()
start = time()
for i in range(10000000):
    myDeck1.size()
finish = time()
print('for instant variable:',(finish - start) * 100)
start = time()
for i in range(10000000):
    myDeck.size()
finish = time()
print('for len(self.cards) method:',(finish - start) * 100)
