from exercise8 import Deck
from time import sleep

class EmptyDeck(Deck):

    def __init__(self):
        self.cards = []

def main():
    mainDeck = Deck()
    playerDeck1 = EmptyDeck()
    playerDeck2 = EmptyDeck()
    mainDeck.shuffleInPlace()
    for i in range(26):
        playerDeck1.addBottom(mainDeck.deal())
        playerDeck2.addBottom(mainDeck.deal())
    print(game(playerDeck1, playerDeck2))

def game(deck1, deck2):
    table = []
    while (deck1.size() != 0) and (deck2.size() != 0):
        p1Card = deck1.deal()
        p2Card = deck2.deal()
        table.append(p1Card)
        table.append(p2Card)
        sleep(0.1)
        while True:
            if compare(p1Card, p2Card) == 'p1':
                for card in table:
                    deck1.addBottom(card)
                table =[]
                break

            elif compare(p1Card, p2Card) == 'p2':
                for card in table:
                    deck2.addBottom(card)
                table = []
                break

            elif compare(p1Card, p2Card) == 'equal':
                try:
                    p1Card = deck1.deal()
                    p2Card = deck2.deal()
                    table.append(p1Card)
                    table.append(p2Card)
                except:
                    break
    
    if deck1.size() == 0:
        return 'Winner is Player 1'
    else:
        return 'Winner is Player 2'

def compare(card1, card2):
    if card1.rank() > card2.rank():
        return 'p1'

    elif card1.rank() < card2.rank():
        return 'p2'

    else:
        return 'equal'

if __name__ == '__main__':
    main()