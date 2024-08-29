import sys

sys.path.insert(0, r'C:\Users\Sina\Documents\DSA_Zelle\chapter2')
from chapter2_exercise12_var import Variable, Polynomial

import unittest

class VariablePolynomialTest(unittest.TestCase):
    def testVariable(self):
        v = Variable(3, 2)
        self.assertEqual(str(v), '3x**2')
    
    def testVariableAdd(self):
        v1 = Variable(3,2)
        v2 = Variable(4,2)
        v1v2 = v1 + v2
        self.assertEqual(str(v1v2), '7x**2')
    
    def testVariableSubstract(self):
        v1 = Variable(5,2)
        v2 = Variable(4,2)
        v1v2 = v1 - v2 
        self.assertEqual(str(v1v2), '1x**2')
    
    def testVariableMultiply(self):
        v1 = Variable(5,2)
        v2 = Variable(3,3)
        v1v2 = v1 * v2
        self.assertEqual(str(v1v2), '15x**5')

    def testPolynomialAdd(self):
        first1 = Variable(2,2)
        second1 = Variable(-4,1)
        third1 = Variable(2)

        first2 = Variable(3,2)
        second2 = Variable(2,1)
        third2 = Variable(2)

        p1 = Polynomial([first1, second1, third1])
        p2 = Polynomial([first2, second2, third2])
        p3 = p1 + p2
        self.assertEqual(str(p3), '5x**2 -2x**1 4x**0')

    def testPolynomialSub(self):
        first1 = Variable(2,2)
        second1 = Variable(-4,1)
        third1 = Variable(2)

        first2 = Variable(3,2)
        second2 = Variable(2,1)
        third2 = Variable(2)

        p1 = Polynomial([first1, second1, third1])
        p2 = Polynomial([first2, second2, third2])
        p3 = p1 - p2
        self.assertEqual(str(p3), '-1x**2 -6x**1 0x**0')
    
    def testPolynomialMul(self):
        first1 = Variable(4,1)
        second1 = Variable(1)

        first2 = Variable(3,1)
        second2 = Variable(2)

        p1 = Polynomial([first1, second1])
        p2 = Polynomial([first2, second2])
        p3 = p1 * p2
        self.assertEqual(str(p3), '12x**2 11x**1 2x**0')

def main(arg):
    unittest.main()

if __name__ == "__main__":
    main(sys.argv)

