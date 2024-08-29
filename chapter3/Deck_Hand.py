import sys
sys.path.insert(0, r'C:\Users\Sina\Documents\DSA_Zelle\chapter2')
from chapter2_Card import Card

from random import randrange

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

    def shuffle(self):
        n = self.size()
        cards = self.cards
        for i,card in enumerate(cards):
            pos = randrange(i,n)
            cards[i] = cards[pos]
            cards[pos] = card

class Hand():
    def __init__(self, label):
        self.label = label
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def sort(self):
        sorted = []
        while self.cards != []:
            card = max(self.cards)
            self.cards.remove(card)
            sorted.append(card)
        self.cards = sorted

    def dump(self):
        print(self.label +"'s Hands:")
        for c in self.cards:
            print('   ', c)

#chapter3_short-answer question
def a():
    myDeck = Deck()
    n = 1
    for i in myDeck.cards:
        print(n, i)
        n += 1
# a()

def b():
    myDeck = Deck()
    myDeck.shuffle()
    for i in range(13):
        return myDeck.deal()
# print(b())

def c(name):
    myHand = Hand(name)
    myDeck = Deck()
    myDeck.shuffle()
    for i in range(13):
        card = myDeck.deal()
        myHand.add(card)
    myHand.sort()
    for i in myHand.cards:
        print(i)

# c()

def d():
    names = ['North', 'East', 'South', 'West']
    for player in names:
        print(player,':')
        c(player)
        print()

# d()