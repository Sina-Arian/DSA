from time import time

'''9.In mathematics Cnk denotes the number of different ways that k things can be selected from among n different choices. For example ...'''

def iter_combinator(n, k):
    nominator = fac(n)
    denominator = fac(k) * fac(n-k)
    return nominator / denominator

def rec_combinator(n, k):
    if k ==1:
        return n
    elif n < k:
        return 0
    else:
        return rec_combinator(n-1, k-1) + rec_combinator(n-1, k)
        

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

start1 = time()
print(iter_combinator(200, 5))
print('iter', time() - start1)
print()
start2 = time()
print(rec_combinator(200, 5))
print('rec', time() - start2)