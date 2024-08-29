'''2.This Exercise is another variation on "instrumenting" the recursive Fibonacci program to ...'''

class FibCounter():
    def __init__(self):
        self.count = 0

    def getCount(self):
        return self.count

    def fib(self, n):
        if n < 3:
            return 1
        else:
            self.count += 2
            return self.fib(n-1) + self.fib(n-2)
        
    def resetCount(self):
        self.count = 0

def main():
    n = int(input("Enter the n: "))
    fib = FibCounter()
    fib.fib(n)
    print(fib.getCount())

main()