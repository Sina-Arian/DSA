import sys
sys.path.append(r'C:\Users\Sina\Documents\DSA_Zelle\chapter4')
import unittest
from PyListCurser import PyCurserList

'''5.Suppose we want out list cursors ...'''

class TestPyListCursor(unittest.TestCase):

    def testBackup(self):
        words = "Curse you and the horse you rode in on".split()
        myCursorList = PyCurserList(words)
        cursor = myCursorList.getCurser()
        cursor.advance()
        cursor.advance()
        cursor.advance()
        cursor.backup()
        self.assertEqual(cursor.getItem(), 'and')

def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)