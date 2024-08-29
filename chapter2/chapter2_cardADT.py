_SUITS = 'cdhs'
_SUITS_NAMES = ['clubs', 'diamonds', 'hearts', 'spades']

_RANKS = list(range(1,14))
_RANKS_NAMES = ['Ace', 'Two', 'Three', 'Four', 'Five',
                'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                'Jack', 'Queen', 'King']

def create(rank,suit)-> tuple:
    assert rank in _RANKS and suit in _SUITS
    return (rank,suit)

def rank(card:tuple):
    return card[0]

def suit(card:tuple):
    return card[1]

def suitName(card:tuple):
    index = _SUITS.index(suit(card))
    return _SUITS_NAMES[index]

def rankName(card:tuple):
    index = _RANKS.index(rank(card))
    return _RANKS_NAMES[index]

def toString(card:tuple):
    return rankName(card) + ' of '+ suitName(card)

