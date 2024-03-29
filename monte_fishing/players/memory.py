import random

from monte_fishing.game import (
        Response,
        Request,
        )

class MemoryPlayer(object):
    def __init__(self,hand):
        self.name="Memory"
        self.hand = {}
        for card in hand:
            if card.value in self.hand:
                self.hand[card.value].append(card)
            else:
                self.hand[card.value] = [card]
        self.opponent_hand = set()

    def request(self):
        valid_choices = set(self.hand.keys()) - self._completed_sets()
        if (any(map(lambda v : v in self.hand.keys(), self.opponent_hand))):
            value = random.choice(list(self.opponent_hand & valid_choices))
        else: 
            try:
                value = random.choice(list(valid_choices))
            except IndexError:
                # No valid choices??
                value = random.choice(list(self.hand.keys()))

        return Request(value)

    def respond(self,request):
        self.opponent_hand.add(request.value)

        if request.value not in self.hand:
            return Response() # Go fish.
        else:
            cards = self.hand[request.value]
            del self.hand[request.value]
            response = Response(cards)
            return response

    def receive_response(self, response):
        if (response.card is not None):
            card_value = response.card[0].value
            if (card_value in self.opponent_hand):
                self.opponent_hand.remove(card_value)
            if (card_value in self.hand):
                self.hand[card_value] = self.hand[card_value] + response.card
            else:
                self.hand[card_value] = response.card

    def sets(self):
        return self.hand 

    def _completed_sets(self):
        completed = set()
        for value in self.hand:
            if (len(self.hand[value]) == 4):
                completed.add(value)
        return completed

    def add_card(self, card):
        if (card.value in self.hand):
            self.hand[card.value].append(card)
        else:
            self.hand[card.value] = [card]


    def __repr__(self):
        return "Memory Player{sets: "+str(len(self.sets()))+" hand: "+str(self.hand)+"}"

