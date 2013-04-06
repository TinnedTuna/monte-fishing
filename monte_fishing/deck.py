import random

class DeckEmptyError():
    pass

class Card():
    """Represents a single card.
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "Card:{Suit:"+self.suit+" value:"+str(self.value)+"}"

class Deck():
    """Represents a deck.
    """
    deck = []
    def __init__(self):
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
        assert type(size) is long
        hand = []
        for i in range(i):
            hand.append(get_card())
        return hand
    
