from time import time
from LList import LList

'''2. Perform an experimental comparison of the efficiency ...'''

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

#linked list is faster than normal list, because every time we add an item we add one single node, but in normal list you have to move the entire items.
#for inserting large amount of file linked list is MUCH faster than normal list