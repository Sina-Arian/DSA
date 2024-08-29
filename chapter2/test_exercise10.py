import sys

sys.path.insert(0, r'C:\Users\Sina\Documents\DSA_Zelle\chapter2') # use your own address

from chapter2_exercise10 import Rational
import unittest

class RationalTest(unittest.TestCase):

    def testConstructorOneInt(self):
        r = Rational(-3)
        self.assertEqual(str(r), '-3/1')

    def testConstructorTwoInt(self):
        r = Rational(9,12)
        self.assertEqual(str(r), '3/4')
    
    def testMul(self):
        r1 = Rational(2,3)
        r2 = Rational(3,4)
        r3 = r1 * r2
        self.assertEqual(str(r3), '1/2')
    
    def testAdd(self):
        r1 = Rational(2,3)
        r2 = Rational(3,4)
        r3 = r1 + r2
        self.assertEqual(str(r3), '17/12')

    def testSub(self):
        r1 = Rational(2,3)
        r2 = Rational(3,4)
        r3 = r1 - r2
        self.assertEqual(str(r3), '-1/12')

    def testDiv(self):
        r1 = Rational(2,5)
        r2 = Rational(4,3)
        r3 = r1 / r2
        self.assertEqual(str(r3), '3/10')

    def testLt(self):
        r1 = Rational(2,5)
        r2 = Rational(4,3)
        r3 = r1 < r2
        self.assertEqual(r3, True)

    def testLe(self):
        r1 = Rational(4,3)
        r2 = Rational(16,12)
        r3 = r1 <= r2
        self.assertEqual(r3, True)

    def testGt(self):
        r1 = Rational(4,3)
        r2 = Rational(3,3)
        r3 = r1 > r2
        self.assertEqual(r3, True)

    def testGe(self):
        r1 = Rational(3,3)
        r2 = Rational(3,3)
        r3 = r1 >= r2
        self.assertEqual(r3, True)

    def testEq(self):
        r1 = Rational(3,3)
        r2 = Rational(3,3)
        r3 = r1 == r2
        self.assertEqual(r3, True)

    def testNe(self):
        r1 = Rational(4,3)
        r2 = Rational(3,3)
        r3 = r1 != r2
        self.assertEqual(r3, True)

def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)