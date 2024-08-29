from time import time
from chapter1_exercise1_algorithms import index_Lsearch, for_Lsearch, Bsearch


lst = range(999999)

target = 1
start = time()
index_Lsearch(lst, target)
finish = time()
print('best time for INDEX method of Linear search is ', (finish - start) * 1000 )
start = time()
for_Lsearch(lst, target)
finish = time()
print('best time for FOR method of Linear search is ', (finish - start) * 1000 )
start = time()
Bsearch(lst, target)
finish = time()
print('best time for  BINARY search is ', (finish - start) * 1000 )
print()

target = 555555
start = time()
index_Lsearch(lst, target)
finish = time()
print('average time for INDEX method of Linear search is ', (finish - start) * 1000 )
start = time()
for_Lsearch(lst, target)
finish = time()
print('average time for FOR method of Linear search is ', (finish - start) * 1000 )
start = time()
Bsearch(lst, target)
finish = time()
print('average time for  BINARY search is ', (finish - start) * 1000 )
print()

target = 999999
start = time()
index_Lsearch(lst, target)
finish = time()
print('worse time for INDEX method of Linear search is ', (finish - start) * 1000 )
start = time()
for_Lsearch(lst, target)
finish = time()
print('worse time for FOR method of Linear search is ', (finish - start) * 1000 )
start = time()
Bsearch(lst, target)
finish = time()
print('worse time for  BINARY search is ', (finish - start) * 1000 )