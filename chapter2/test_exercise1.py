import sys
import unittest

sys.path.insert(0, r'C:\Users\Sina\Documents\DSA_Zelle\chapter2') # use your own address
from chapter2_exercise2 import *

class CardTest(unittest.TestCase):

    def testClassString(self):
        myCard = Card(37)
        self.assertEqual(str(myCard),'Queen of hearts')

    def testSuit(self):
        myCard = Card(37)
        self.assertEqual(myCard.suit(), 2)

    def testRank(self):
        myCard = Card(37)
        self.assertEqual(myCard.rank(), 11)

    def testRankName(self):
        myCard = Card(37)
        self.assertEqual(myCard.rankName(), 'Queen')

    def testSuitName(self):
        myCard = Card(37)
        self.assertEqual(myCard.suitName(), 'hearts')

def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
