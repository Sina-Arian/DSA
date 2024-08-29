from Deck_Hand import Deck
from random import shuffle

class NewDeck(Deck):
    def shuffle(self):
        shuffle(self.cards)

myDeck = NewDeck()
myDeck.shuffle()
print(myDeck.deal())
