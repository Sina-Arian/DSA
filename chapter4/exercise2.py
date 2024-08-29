from time import time
from LList import LList

start = time()
normal_list = []
for i in range(150000):
    normal_list.insert(0, i)
print(time() - start, 'for the normal list')


start = time()
linked_list = LList()
for i in range(15000000):
    linked_list.insert(0, i)
print(time() - start, 'for the linked list')