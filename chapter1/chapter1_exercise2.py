from time import time
from random import randint

ten_thousands = []
for i in range(10000):
    ten_thousands.append(randint(1, 10000000))
start = time()
ten_thousands.sort()
finish = time()
print('for 10000 unsorted list it takes ', (finish - start) * 1000 , ' to being sorted.')

oneHundred_thousands = []
for i in range(100000):
    oneHundred_thousands.append(randint(1, 10000000))
start = time()
oneHundred_thousands.sort()
finish = time()
print('for 100000 unsorted list it takes ', (finish - start) * 1000 , ' to being sorted.')

oneMilion = []
for i in range(1000000):
    oneMilion.append(randint(1, 10000000))
start = time()
oneMilion.sort()
finish = time()
print('for 1000000 unsorted list it takes ', (finish - start) * 1000 , ' to being sorted.')