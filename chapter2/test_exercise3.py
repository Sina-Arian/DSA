import sys
import unittest

sys.path.insert(0, r'C:\Users\Sina\Documents\DSA_Zelle\chapter2') # use your own address
from chapter2_exercise3 import *

class DeckTest(unittest.TestCase):
    
    def TestDeal(self):
        myDeck = Deck()
        self.assertEqual(myDeck.deal(), None)

    def TestCardLeft(self):
        myDeck = Deck()
        self.assertEqual(type(myDeck.cardLeft()), type('wswetfr'))


def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)