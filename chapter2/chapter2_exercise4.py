
import sys

sys.path.insert(0, '.')
from button import Button
from graphics import *
from chapter2_exercise3 import Deck
from time import sleep

def game(myDeck:object):
        win = GraphWin('Blackjack', 800, 600)
        win.setCoords(0, 0, 10, 10)
        win.setBackground('green')
        message = Text(Point(4.5, 5), 'click to play: ')
        message.draw(win)
        hit = Button(win, Point(3,5), 0.5, 0.5, 'Hit')
        hit.activate()
        pas = Button(win, Point(6,5), 0.5, 0.5, 'Pass')
        pas.activate()
        card_left = Text(Point(8, 5),f'card left:{myDeck.cardLeft()}')
        card_left.draw(win)
        while myDeck.cardLeft() != 0:
            dealer = []
            player = []
            for i in range(2):
                newCard = myDeck.deal()
                dealerCard = myDeck.deal()
                if newCard.rank() == 0:
                    player.append(newCard)
                else:
                    player.insert(0, newCard)

                if dealerCard.rank() == 0:
                    dealer.append(dealerCard)
                else:
                    dealer.insert(0, dealerCard)

            card_left.setText(f'card left:{myDeck.cardLeft()}')

            x = 2
            for i in player:
                i.draw(win, Point(x, 2))
                x += 1

            z = 2
            for i in dealer:
                i.draw(win, Point(z, 8))
                z += 1

            #playerTime
            dealertime = False
            while True:
                message.setText('click to play: ')
                choose = win.getMouse()

                if hit.clicked(choose) == True:
                    newCard = myDeck.deal()
                    newCard.draw(win, Point(x,2))
                    x += 1
                    
                    if newCard.rank() == 0:
                        player.append(newCard)
                    else:
                        player.insert(0, newCard)

                    card_left.setText(f'card left:{myDeck.cardLeft()}')

                    if total(player) == 21:
                        message.setText('player wins')
                        win.getMouse()
                        break

                    elif total(player) > 21:
                        message.setText('player busted')
                        win.getMouse()
                        break

                elif pas.clicked(choose) == True:
                    dealertime = True
                    break
                
                else:
                    message.setText('choose Hit or pass')
                    continue
        
            #dealerTime
            if dealertime == True:
                while True:

                    if (total(dealer) > total(player)) and total(dealer) < 22:
                        message.setText('dealer wins')
                        win.getMouse()
                        break

                    elif total(dealer) == total(player):
                        message.setText('player wins')
                        win.getMouse()
                        break

                    elif total(dealer) > 21:
                        message.setText('dealer busted player wins')
                        win.getMouse()
                        break
                    sleep(1)
                    dealerCard = myDeck.deal()
                    dealerCard.draw(win, Point(z, 8))
                    z += 1

                    if dealerCard.rank() == 0:
                        dealer.append(dealerCard)
                    else:
                        dealer.insert(0, dealerCard)
                    
                    card_left.setText(f'card left:{myDeck.cardLeft()}')
            for i in player:
                i.undraw()
            for i in dealer:
                i.undraw()

def total(lst):
    sum = 0
    for i in lst:
        if (i.rank() + 1) > 10: #its a face
            sum += 10

        elif (i.rank() + 1) == 1 and (sum + (i.rank() + 11) < 22) : #its an ace
            sum += 11
            
        else:
            sum += i.rank() + 1 #its a normal number
            
    return sum

def worth(card):
    if (card.rank() + 1) > 10:
        return 10
    else:
        return card.rank() + 1

def main():
    for i in range(10):
        myDeck = Deck()
        game(myDeck)
  
main()