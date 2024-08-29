from time import time
from chapter1_exercise1_algorithms import index_Lsearch, Bsearch
import matplotlib.pyplot as plt
from random import randint

Y1 = []
Y2 = []
X = list(range(1, 1000))

for n in X:
    lst = []
    for i in range(n):
        lst.append(randint(1,100))
    target = lst[-1]
    print(lst)

    start = time()
    for t in range(500000):
        index_Lsearch(lst, target)
    finish = time()
    out1 = (Y1).append((finish - start) * 10000)

    start = time()
    for t in range(500000):
        Bsearch(lst, target)
    finish = time()
    out2 = (Y2).append((finish - start) * 10000)


plt.plot(X, Y1, label="linear search")
plt.plot(X, Y2, label = "binary search")

plt.xlabel('list size')
plt.ylabel('time')

plt.legend()
plt.show()