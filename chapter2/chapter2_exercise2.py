import sys

sys.path.insert(0, r'C:\Users\Sina\Documents\DSA_Zelle') # use your own system address
from graphics import *

'''2. Implement the Card class ...'''

class Card:
    """A simple playing card. A Card is characterized by two components.
    rank: an integer value in the range  1-13, inclusive (Ace-King)
    suit: a character in 'cdhs' for clubs, diamonds, hearts, and
          spades."""
    
    _SUITS = 'cdhs'

    _SUITS_NAMES = ['clubs', 'diamonds', 'hearts', 'spades']

    _RANKS_NAMES = ['Ace', 'Two', 'Three', 'Four', 'Five',
                'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                'Jack', 'Queen', 'King']

    def __init__(self, number):
        """Constructor
        pre: rank in range(1,14) and suit in 'cdhs'
        post: self has the given rank and suit"""
        self.card_num = number
        self.x = 0
        self.y = 0

    def suit(self):
        """Card suit
        post: Returns the suit of self as a single character"""
        return self.card_num // 13

    def rank(self):
        return self.card_num % 13
    
    def suitName(self):
        return self._SUITS_NAMES[self.suit()]

    def rankName(self):
        return self._RANKS_NAMES[self.rank()]

    def draw(self, win, center):
        filename = self.rankName() + '_of_'+ self.suitName()
        self.img = Image(center,  'C:\\Users\\Sina\\Documents\\DSA_Zelle\\cards_pics\\'+ filename +'.png') # use your own address
        self.img.draw(win)
        self.x = center.getX()
        self.y = center.getY()

    def undraw(self):
        self.img.undraw()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return self.rankName() + ' of '+ self.suitName()
