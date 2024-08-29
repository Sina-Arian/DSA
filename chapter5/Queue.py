class Queue:
    def __init__(self):
        self.FIFO = []

    def inqueue(self, x):
        self.FIFO.append(x)

    def dequeue(self):
        return self.FIFO.pop(0)

    def top(self):
        return self.FIFO[0]

    def size(self):
        return len(self.FIFO)
        