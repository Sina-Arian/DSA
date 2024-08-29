'''2.Implement the Card class using the alternative representation ...'''



class Card:
    """A simple playing card. A Card is characterized by two components.
    rank: an integer value in the range  1-13, inclusive (Ace-King)
    suit: a character in 'cdhs' for clubs, diamonds, hearts, and
          spades."""
    _SUITS = 'cdhs'
    _SUITS_NAMES = ['clubs', 'diamonds', 'hearts', 'spades']

    _RANKS = list(range(2,15))
    _RANKS_NAMES = ['Two', 'Three', 'Four', 'Five',
                'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, rank, suit):
        """Constructor
        pre: rank in range(1,14) and suit in 'cdhs'
        post: self has the given rank and suit"""
        self.rank_num = rank
        self.suit_char = suit

    def suit(self):
        """Card suit
        post: Returns the suit of self as a single character"""
        return self.suit_char

    def rank(self):
        return self.rank_num
    
    def suitName(self):
        index = self._SUITS.index(self.suit_char)
        return self._SUITS_NAMES[index]

    def rankName(self):
        index = self._RANKS.index(self.rank_num)
        return self._RANKS_NAMES[index]

    def __str__(self):
        return self.rankName() + ' of '+ self.suitName()
        
    
    def __eq__(self, other):
        return ((self.suit_char == other.suit_char) and 
                (self.rank_num == other.rank_num))

    def __lt__(self, other):
        if self.suit_char == other.suit_char:
            return self.rank_num < other.rank_num
        else:
            return self.suit_char < other.suit_char
    
    def __ne__(self, other):
        return not(self == other)

    def __le__(self, other):
        return (self < other) or (self == other)
