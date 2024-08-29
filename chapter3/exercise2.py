from Deck_Hand import Deck
from random import shuffle

'''2.Look into the functions provided by the Python random module ...'''

class NewDeck(Deck):
    def shuffle(self):
        shuffle(self.cards)

myDeck = NewDeck()
myDeck.shuffle()
print(myDeck.deal())
