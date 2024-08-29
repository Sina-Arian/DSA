'''7. Computer scientist and mathematicians often use numbering systems other than ...'''


def printDigits(n,base):
    if n < base:
        return [n]
    else:
        return [*printDigits(n//base, base), n % base]



def main():
    n = 153 #int(input("Enter the number: "))
    base = 10 #int(input("Enter the base: "))
    res = printDigits(n,base) # it return a tuple
    for i in res:
        print(i, end= ' ')
    print()

main()
