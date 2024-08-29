class Stack:

    def __init__(self):
        self.LIFO = []

    def push(self, x):
        self.LIFO.append(x)

    def pop(self):
        return self.LIFO.pop()

    def top(self):
        return self.LIFO[-1]

    def size(self):
        return len(self.LIFO)