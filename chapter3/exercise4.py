from Deck_Hand import Deck
from random import randint


class NewDeck(Deck):
    def randomCard(self):
        n = self.size()
        x = randint(0, n)
        return self.cards.pop(x)

myDeck = NewDeck()
print(myDeck.randomCard())
print(myDeck.size())