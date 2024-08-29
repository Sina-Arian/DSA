from exercise4 import queueInOrder, permInOrder
from Stack import Stack
from Queue import Queue
from time import sleep

'''7.The previous exercise involves simulating the marble clock until the reservir ...'''

class Permutation():
    def __init__(self, item, ind):
        self.item = item
        self.perm = ind

    def permut(self):
        return self.perm


def marbleClock(n):
    reservoir = Queue()
    first = Stack()
    second = Stack()
    third = Stack()
    third.push('Fixed')
    for i in range(n):
        reservoir.inqueue(Permutation(i,i))
    
    cycle = 0
    while True:
        marble = reservoir.dequeue()
        
        first.push(marble)
        if first.size() == 5:
            while first.size() != 1:
                reservoir.inqueue(first.pop())
            marble = first.pop()
            second.push(marble)
        
        if second.size() == 12:
            while second.size() != 1:
                reservoir.inqueue(second.pop())
            marble = second.pop()
            third.push(marble)
        
        if third.size() == 12:
            while third.size() != 1:
                reservoir.inqueue(third.pop())
            
            out = []
            for i in range(reservoir.size()):
                x = reservoir.dequeue()
                out.append(x.permut())
                reservoir.inqueue(x)

            if permInOrder(out):
                break
        
            cycle += 1

        # sleep(0.0002)

    return cycle
    

print(marbleClock(27))