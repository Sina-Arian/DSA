from time import time
from chapter1_exercise1_algorithms import index_Lsearch, Bsearch
import matplotlib.pyplot as plt

'''4.Design your own experiment to compare the behavior ...'''


Y1 = []
Y2 = []
X = list(range(1000))

for n in X:
    lst = list(range(n))
    target = len(lst)
    

    start = time()
    for t in range(1000):
        index_Lsearch(lst, target)
    finish = time()
    out1 = (Y1).append((finish - start) * 10000)

    start = time()
    for t in range(1000):
        Bsearch(lst, target)
    finish = time()
    out2 = (Y2).append((finish - start) * 10000)


plt.plot(X, Y1, label="linear search")
plt.plot(X, Y2, label = "binary search")

plt.xlabel('list size')
plt.ylabel('time')

plt.legend()
plt.show()