import random

class DeckEmptyError(Exception):
    pass

class Card():
    """Represents a single card.
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "Card:{Suit:"+self.suit+" value:"+str(self.value)+"}"

    def __eq__(self,other):
        return (other.suit == self.suit and other.value == self.value) 

    def __ne__(self,other):
        return not (other.suit == self.suit and other.value == self.value) 

    def __hash__(self):
        h = 5;
        incl = 7;
        h = h * self.suit.__hash__() + incl;
        h = h * self.value.__hash__() + incl;
        return h

class Deck():
    """Represents a deck.
    """
    def __init__(self):
        self.deck = []
        for suit in ['Hearts','Spades','Diamonds','Clubs']:
            for value in range(1,14):
                self.deck.append(Card(suit,value))
        random.shuffle(self.deck)

    def get_card(self):
        try: 
            card = self.deck.pop()
        except IndexError:
            raise DeckEmptyError()
        return card

    def get_hand(self, size):
        assert (type(size) is long) or (type(size) is int)
        hand = []
        for i in range(size):
            hand.append(self.get_card())
        return hand
    
