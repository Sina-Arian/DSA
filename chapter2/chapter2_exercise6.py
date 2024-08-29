from chapter2_exercise5 import solitare
from chapter2_exercise3 import Deck

'''6.Modify the previous exercise so that is calculates ...'''

def main():
    pile_number = int(input('Enter the number of piles: '))
    win = 0
    for i in range(1000):
        res = solitare(Deck(), pile_number, False, 0.000000000001)
        if res == 'You Won':
            win += 1
    return (win/1000) * 100

print(main())