'''8.Write a recursive function to print out the digits of a number in English. For example, if ...'''

def typeout(n):
    if n < 10:
        return [printOut(n)]
    
    else:
        return [*typeout(n // 10), printOut(n % 10)]


def printOut(n):
    table = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return table[n]

print(typeout(268))