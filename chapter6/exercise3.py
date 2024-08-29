'''Write a recursive function that implement tha same algorithm as the looping version of the nth Fibnonacci ...'''


def fib(a,b,n):
    if n == 0:
        return b
    else:
        temp = b
        b = b + a
        a = temp
        n -= 1
        return fib(a, b, n)


def main():
    n = int(input("Enter the nth fib number: "))
    n -= 2 # cuz you gave the first 2 number already ( 1 and 1)
    print(fib(1,1,n))


main()