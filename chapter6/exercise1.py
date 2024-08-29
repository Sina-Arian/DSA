'''1.Modify the recursive Fibonacci program given in the chapter so that ...'''


def recFib(n):
    print('calculating Fib({})'.format(n))
    if n < 3:
        print('leaving Fib({}) returning 1'.format(n))
        return 1
    else:
        print('leaving Fib({}) returning Fib({}) and Fib({})'.format(n, n-1, n-2))
        return recFib(n-1) + recFib(n-2)
        
recFib(10)