import sys
sys.path.insert(0, '.')

from chapter2_exercise3 import Deck
from graphics import *
from time import sleep

'''5.Using the Deck class from exercise 3, write a program that plays a simple solitaire game ... '''

def solitare(myDeck:object, pile_num:int, GUI=True, delay=1):
    if GUI == True:
        win = GraphWin('Solitare', 1250, 1000)
        win.setCoords(0, 0, 12.5, 10)
        win.setBackground('green')
    piles = []
    for i in range(pile_num):
        piles.append(myDeck.deal())

    if GUI == True:
        x = 1
        y = 9
        for p in piles:
            p.draw(win, Point(x,y))
            x += 1.5

    condi = False
    same = cnt(piles) #objects with same rank
    while (myDeck.cardLeft() != 0) and (len(same) != 0):
        sleep(delay)
        for c in same:
            try:
                new = myDeck.deal()
            except:
                condi = True
            if GUI == True:
                old_x = c.getX()
                old_y = c.getY()
                new.draw(win, Point(old_x, old_y - 0.35))
            sub(piles, c, new) #its a mutator
        same = cnt(piles)
        if myDeck.cardLeft() == 0:
            condi = True
    if GUI == True:
        win.getMouse()
        win.close()
    if len(same) == 0:
        return 'You Lose'
    elif condi == True:
        return 'You Won'

def sub(lst, old, new):
    old_index = lst.index(old)
    lst.pop(old_index)
    lst.insert(old_index, new)
    return lst

def cnt(pile:list):
    ranks = []
    chosen = []
    for i in pile:
        ranks.append(i.rank())
    for i in pile:
        if ranks.count(i.rank()) >= 2:
            chosen.append(i)
    return chosen

def main():
    n = 8 # between 1 to 8
    myDeck = Deck()
    print(solitare(myDeck, n))


if __name__ == '__main__':
    main()