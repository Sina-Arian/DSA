from exercise4 import queueInOrder
from Stack import Stack
from Queue import Queue
from time import sleep

'''6.A marble clock is a novelty timepiece that shows the current time via ...'''

def marbleClock(n):
    reservoir = Queue()
    first = Stack()
    second = Stack()
    third = Stack()
    third.push('Fixed')
    for i in range(n):
        reservoir.inqueue(i)
    
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
            
            if queueInOrder(reservoir):
                break
            cycle += 1

        # sleep(0.0002)

    return cycle



print(marbleClock(27))