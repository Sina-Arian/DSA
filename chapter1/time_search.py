from time import time
from bsearch import search

items = range(10000000)
start = time()
print(search(items, 9999999))
finish = time()
print(finish - start)

start = time()
print(search(items, 5555555))
finish = time()
print(finish - start)

start = time()
print(search(items, 10))
finish = time()
print(finish - start)

