from Queue import Queue
from time import sleep

'''8.The number of times a permutation must be applied before it restores a sequence ...'''

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
        self.line = Queue()
        self.serviceTime = 0
        self.totalWait = 0
        self.maxWait = 0
        self.customerCount = 0
        self.maxLength = 0
        self.ticksPerItem = avgTime

    def clockTick(self):
        while self.arrivals.size() != 0 and (self.line.size() == 0 or self.arrivals.top().arrivalTime <= self.time):
                self.line.inqueue(self.arrivals.dequeue())
        self.maxLength = max(self.maxLength, self.line.size())
        
        customer = self.line.dequeue()
        self.customerCount += 1
        serviceTime = customer.items * self.ticksPerItem
        waitTime = self.time - customer.arrivalTime
        if waitTime < 0:
            waitTime = 0
            self.time += customer.arrivalTime
        self.totalWait += waitTime
        self.maxWait = max(self.maxWait, waitTime)
        self.time += serviceTime


    def averageWait(self):
        return float(self.totalWait) / self.customerCount

    def maximumWait(self):
        return self.maxWait

    def maximumLineLength(self):
        return self.maxLength

    def run(self):
        while (self.arrivals.size() > 0 or self.line.size() > 0):
            self.clockTick()

def main():
    q = makingQueue('customerList.txt')
    sim = CheckerSim(q, 4)
    sim.run()
    print('average wait time', sim.averageWait(), '\nmaximum line length', sim.maximumLineLength(), '\nmaximum wait', sim.maximumWait())

main()
