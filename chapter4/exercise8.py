from copy import deepcopy, copy
from LList import LList
from LList_cursor import *

'''8.The Sieve of Eratosthenes is famouse algorithm for ...'''

def sieveOfEratosthenes(number_list) -> list:

    primeCursor = number_list.getCurser()
    while not primeCursor.done():

        prime = primeCursor.getItem()
        checkCursor = copy(primeCursor)
        checkCursor.advance()

        while not checkCursor.done():
            item = checkCursor.getItem()
            if (item % prime) == 0:
                checkCursor.deleteItem()
            else:
                checkCursor.advance()

        primeCursor.advance()

    return number_list

def main():
    n = int(input("Enter the number to find prims to it: "))
    number_list = LinkedCursorList()
    for i in range(2, n):
        number_list.append(i)

    linked_list_res = sieveOfEratosthenes(number_list)
    for i in linked_list_res:
        print(i)

main()