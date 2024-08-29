from LList import LList, ListNode

class LinkedCursorList(LList):

    def getCurser(self):
        return LListCurser(self)


class LListCurser():

    def __init__(self, llist: LList):
        self.lst = llist
        self.header = ListNode("**DUMMY HEADER NODE**", llist.head)
        self.prev = self.header

    def __copy__(self):
        c = LListCurser(self.lst)
        c.prev = self.prev
        return c

    def done(self):
        return self.prev.link is None

    def getItem(self):
        return self.prev.link.data

    def replaceItem(self, value):
        self.prev.link.data = value

    def deleteItem(self):
        self.prev.link = self.prev.link.link
        self.lst.head = self.header.link

    def insertItem(self, value):
        new_node = ListNode(value, self.prev.link)
        self.prev.link = new_node
        self.advance()

    def advance(self):
        self.prev = self.prev.link

    def backup(self):
        self.prev = self.prev.before

