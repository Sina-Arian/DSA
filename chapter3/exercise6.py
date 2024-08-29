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

    def dump(self):
        print(self.label +"'s Hands:")
        for c in self.cards:
            print('   ', c)