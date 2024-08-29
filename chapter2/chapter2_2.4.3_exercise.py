from math import sqrt

class Dataset:
    def __init__(self):
        self._size = 0
        self._min = 0.0
        self._max = 0.0
        self._sum = 0.0
        self._sum_squares = 0.0

    def add(self, x):
        self._size += 1.0
        if x < self._min:
            self._min = x
        elif x > self._max:
            self._max = x
        self._sum += x
        self._sum_squares += (x**2)

    def min(self):
        return self._min

    def max(self):
        return self._max

    def average(self):
        return self._sum / self._size

    def std_deviation(self):
        soorat = ((self._sum_squares)**2) - ((self._sum)**2 / self._size)
        return sqrt(soorat / (self._size - 1))