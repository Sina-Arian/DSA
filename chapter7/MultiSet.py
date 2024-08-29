from BST import BST
from KeyPair import KeyPair

'''7.Implement and test an ordered multi_set class based on a BST. A multi_set is a set that allows multiple ...'''

class MultiSet():
    def __init__(self):
        self.items = BST()
        self.lentgh = 0

    def delete(self, item):
        self.items.delete(KeyPair(item))
        return f"all of the {item}(s) get deleted"
        
    def insert(self, item):
        IWantThisKey = KeyPair(item)
        HereItIs = self.items.find(IWantThisKey)
        if HereItIs is None:
            self.items.insert(KeyPair(item))
        else:
            HereItIs.number += 1

    def count(self, item):
        IWantThis = self.items.find(KeyPair(item))
        if IWantThis is None:
            return 0
        else:
            return IWantThis.number

    def __iter__(self):
        for i in self.items:
            for n in range(i.number):
                yield i.value

    def __len__(self):
        total = 0
        for i in self.items:
            total += i.number
        return total
