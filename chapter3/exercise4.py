from Deck_Hand import Deck
from random import randint

'''4.Instead of shuffling a deck of cards, ...'''

class NewDeck(Deck):
    def randomCard(self):
        n = self.size()
        x = randint(0, n)
        return self.cards.pop(x)

myDeck = NewDeck()
print(myDeck.randomCard())
print(myDeck.size())