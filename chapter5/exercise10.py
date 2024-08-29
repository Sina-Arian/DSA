from Queue import Queue
from time import sleep
from random import random

'''10.Suppose our retail store is going to upgrade ...'''

class Customer():
    def __init__(self, arrivalTime, items):
        self.arrivalTime = int(arrivalTime)
        self.items = int(items)

    def __repr__(self):
        return f'Customer time arrival {self.arrivalTime}, items {self.items}'

# class Queue(Queue):
#     def top(self):
#         if self.FIFO == []:
#             return None


def makingQueue(file):
    queue = Queue()
    inFile = open(file, 'r')
    for line in inFile:
        time, item = line.split()
        queue.inqueue(Customer(time, item ))
    inFile.close()
    return queue




class CheckerSim():

    def __init__(self, arrivalQueue:Queue, avgTime:0):
        self.time = 0
        self.arrivals = arrivalQueue
        self.line1 = Queue()
        self.line2 = Queue()
        self.serviceTime = 0
        self.serviceTime2 = 0
        self.totalWait = 0
        self.maxWait = 0
        self.customerCount = 0
        self.maxLength1 = 0
        self.maxLength2 = 0
        self.ticksPerItem = avgTime

    def clockTick(self):
        self.time += 1
        while self.arrivals.size() > 0 and self.arrivals.top().arrivalTime == self.time:
            if self.line1.size() < self.line2.size():
                self.line1.inqueue(self.arrivals.dequeue())

            elif self.line1.size() > self.line2.size():
                self.line2.inqueue(self.arrivals.dequeue())

            else:
                r = random()
                if r > .5:
                    self.line1.inqueue(self.arrivals.dequeue())
                else:
                    self.line2.inqueue(self.arrivals.dequeue())
            self.customerCount += 1

        self.maxLength1 = max(self.maxLength1, self.line1.size())
        self.maxLength2 = max(self.maxLength2, self.line2.size())
        
        if self.serviceTime > 0:
            self.serviceTime -= 1
        elif self.line1.size() > 0:
            customer = self.line1.dequeue()
            self.serviceTime = customer.items * self.ticksPerItem
            waitTime = self.time - customer.arrivalTime
            self.totalWait += waitTime
            self.maxWait = max(self.maxWait, waitTime)


        if self.serviceTime2 > 0:
            self.serviceTime2 -= 1
        elif self.line2.size() > 0:
            customer2 = self.line2.dequeue()
            self.serviceTime2 = customer2.items * self.ticksPerItem
            waitTime2 = self.time - customer2.arrivalTime
            self.totalWait += waitTime2
            self.maxWait = max(self.maxWait, waitTime2)


    def averageWait(self):
        return float(self.totalWait) / self.customerCount

    def maximumWait(self):
        return self.maxWait

    def maximumLineLength(self):
        return max(self.maxLength1, self.maxLength2)

    def run(self):
        while (self.arrivals.size() > 0 or self.line1.size() > 0 or self.line2.size() > 0):
            self.clockTick()

def main():
    q = makingQueue('customerList.txt')
    sim = CheckerSim(q, 4)
    sim.run()
    print('average wait time', sim.averageWait(), '\nmaximum line length', sim.maximumLineLength(), '\nmaximum wait', sim.maximumWait())

main()
