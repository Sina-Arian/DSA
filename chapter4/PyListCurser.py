'''5.Suppose we want out list cursors to be able to move ...'''


class PyListCurser:

    def __init__(self, pylist):
        self.index = 0
        self.lst = pylist

    def done(self):
        return self.index == len(self.lst)

    def getItem(self):
        return self.lst[self.index]

    def replaceItem(self, value):
        self.lst[self.index] = value

    def deleteItem(self):
        del self.lst[self.index]

    def insertItem(self, value):
        self.lst.insert(self.index, value)
    
    def advance(self):
        self.index += 1

    def backup(self): # IMPORTANT: remember header is in index = -1 so you have to implement an condition that if self.index = 0, returns the first 
        self.index -= 1


class PyCurserList(list):

    def getCurser(self):
        return PyListCurser(self)

