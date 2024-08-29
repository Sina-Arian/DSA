from Deck_Hand import Deck
import random

'''3.Suppose we want to be able to place cards back into a deck...'''

class NewDeck(Deck):
    def addTop(self, card):
        self.cards.insert(0, card)
    
    def addBottom(self, card):
        self.cards.append(card)

    def addRandom(self, card):
        ind = random.randint(0, 52)
        self.cards.insert(ind, card)

