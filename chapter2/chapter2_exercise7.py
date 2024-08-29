from math import sqrt

class Dataset1:
    def __init__(self):
        self.data = []
    
    def size(self):
        return len(self.data)

    def add(self, number):
        self.data.append(number)

    def min(self):
        min = self.data[0]
        for i in self.data:
            if i < min:
                min = i
        return min

    def max(self):
        max = self.data[0]
        for i in self.data:
            if i > max:
                max = i
        return max

    def average(self):
        sum = 0
        num = 0
        for i in self.data:
            sum += i
            num += 1
        return sum/num
    
    def std_deviation(self):
        soorat = 0
        for i in self.data:
            a = (self.average() - i) ** 2
            soorat += a
        makhraj = len(self.data) - 1
        return sqrt(soorat/makhraj)
    

class Dataset2:
    def __init__(self):
        self._size = 0
        self._min = None
        self._max = 0
        self._sum = 0
        self._sum_squares = 0

    def size(self):
        return self._size
    
    def min(self):
        return self._min
    
    def max(self):
        return self._max

    def average(self):
        return self._sum/self._size
    
    def add(self, number):
        if self._min == None:
            self._min = number
        self._size += 1
        if number < self._min:
            self._min = number
        if number > self._max:
            self._max = number
        self._sum += number
        self._sum_squares += (number) ** 2
    
    def std_deviation(self):
        nominator = self._sum_squares- ((self._sum) ** 2 / self._size)
        denominator = self._size - 1
        return sqrt(nominator/denominator)