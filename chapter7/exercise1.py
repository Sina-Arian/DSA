import sys
sys.path.insert(0, r'C:\Users\Sina\Documents\DSA_Zelle\chapter7\BST.py')
from BST import BST
import unittest

class BSTTest(unittest.TestCase):
    def testBST(self):
        myBST = BST()
        for i in range(10): myBST.insert(i)
        res = []
        for i in myBST: res.append(i)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(res, expected)

    def testRecInsert(self):
        myBST = BST()
        for i in range(10): myBST.insert_rec(i)
        res = []
        for i in myBST: res.append(i)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(res, expected)

    def testDelete(self):
        myBST = BST()
        for i in range(10): myBST.insert_rec(i)
        myBST.delete(5)
        res = []
        for i in myBST: res.append(i)
        expected = [0, 1, 2, 3, 4, 6, 7, 8, 9]
        self.assertEqual(res, expected)

    def testDelete_succ(self):
        myBST = BST()
        for i in range(10): myBST.insert_rec(i)
        myBST.delete_succ(5)
        res = []
        for i in myBST: res.append(i)
        expected = [0, 1, 2, 3, 4, 6, 7, 8, 9]
        self.assertEqual(res, expected)

    def testFind(self):
        myBST = BST()
        for i in range(10): myBST.insert_rec(i)
        res = myBST.find(4)
        self.assertEqual(res, 4)
    
    def testFind_rec(self):
        myBST = BST()
        for i in range(10): myBST.insert_rec(i)
        self.assertEqual(myBST.find(9), myBST.find_rec(10))

def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)