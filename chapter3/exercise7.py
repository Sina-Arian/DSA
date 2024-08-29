'''7.Another way to put a hand in order is to place each card into'''

class Hand():
    def __init__(self, label):
        self.label = label
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def sort(self):
        cards = self.cards
        for i,card in enumerate(cards):
            new_card = max(cards)
            new_card_index = cards.index(new_card)
            cards[new_card_index], cards[i] = card, new_card
        return cards

    def insertion_sort(self, card):
        if self.cards == []:
            self.cards.append(card)
        else:
            for item in self.cards:
                _in = False
                if card > item:
                    ind = self.cards .index(item)
                    self.cards .insert(ind, card)
                    _in = True
                    break

            if _in == False:
                self.cards .append(card)
                
        return self.cards 

    def dump(self):
        print(self.label +"'s Hands:")
        for c in self.cards:
            print('   ', c)