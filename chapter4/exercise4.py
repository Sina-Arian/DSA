import sys
sys.path.append(r'C:\Users\Sina\Documents\DSA_Zelle\chapter4')
from LList_cursor import LinkedCursorList

import unittest

'''4.Finish the implementation of the LListCursor ... '''

class LinkedCursorListTest(unittest.TestCase):

    def testLinkedCursorList(self):
        sentence = ['Curse', 'you', 'and', 'the', 'horse', 'you', 'rode', 'in', 'on']
        words_cursed = LinkedCursorList(sentence)
        curser = words_cursed.getCurser()
        self.assertEqual(curser.header.data, '**DUMMY HEADER NODE**')

    def testgetItem(self):
        sentence = ['Curse', 'you', 'and', 'the', 'horse', 'you', 'rode', 'in', 'on']
        words_cursed = LinkedCursorList(sentence)
        curser = words_cursed.getCurser()
        self.assertEqual(curser.getItem(), 'Curse')

    def testreplaceItem(self):
        sentence = ['Curse', 'you', 'and', 'the', 'horse', 'you', 'rode', 'in', 'on']
        words_cursed = LinkedCursorList(sentence)
        curser = words_cursed.getCurser()
        curser.replaceItem('Sina')
        self.assertEqual(curser.getItem(), 'Sina')

    def testdeleteItem(self):
        sentence = ['Curse', 'you', 'and', 'the', 'horse', 'you', 'rode', 'in', 'on']
        words_cursed = LinkedCursorList(sentence)
        curser = words_cursed.getCurser()
        curser.deleteItem()
        self.assertEqual(curser.getItem(), 'you')

    def testinsertItem(self):
        sentence = ['Curse', 'you', 'and', 'the', 'horse', 'you', 'rode', 'in', 'on']
        words_cursed = LinkedCursorList(sentence)
        curser = words_cursed.getCurser()
        curser.insertItem('Jafar')
        self.assertEqual(curser.prev.data, 'Jafar')

    def testAdvance(self):
        sentence = ['Curse', 'you', 'and', 'the', 'horse', 'you', 'rode', 'in', 'on']
        words_cursed = LinkedCursorList(sentence)
        curser = words_cursed.getCurser()
        curser.advance()
        self.assertEqual(curser.getItem(), 'you')

    def testBackup(self):
        sentence = ['Curse', 'you', 'and', 'the', 'horse', 'you', 'rode', 'in', 'on']
        words_cursed = LinkedCursorList(sentence)
        curser = words_cursed.getCurser()
        curser.advance()
        curser.advance()
        curser.advance()
        curser.advance()
        curser.backup()
        curser.backup()
        self.assertEqual(curser.getItem(), 'and')

def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)