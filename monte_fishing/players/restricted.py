import random

from monte_fishing.game import (
        Response,
        Request,
        )

class Memory(object):
    def __init__(self):
        self.opponents_cards = []

    def seen(self, card_value):
        if (card_value not in self.opponents_cards):
            self.opponents_cards.append(card_value)
        if (len(self.opponents_cards) > 3):
            self.opponents_cards[:3]

    def remove(self, card_value):
        if (card_value in self.opponents_cards):
            self.opponents_cards.remove(card_value)

    def memory(self):
        return set(self.opponents_cards)

class RestrictedMemoryPlayer(object):
    def __init__(self,hand):
        self.name="Restricted"
        self.hand = {}
        self.completed = {}
        for card in hand:
            self.add_card(card)
        self.memory = Memory()

    def _update_completed(self):
        change = []
        for card_value in self.hand:
            if (len(self.hand[card_value]) == 4):
                self.completed[card_value] = self.hand[card_value]
                change.append(card_value)
        for c in change:
            del self.hand[c]

    def request(self):
        valid_choices = set(self.hand.keys()) - self._completed_sets()
        if (any(map(lambda v : v in self.hand.keys(), self.memory.memory()))):
            value = random.choice(list(self.memory.memory() & valid_choices))
        else: 
            try:
                value = random.choice(list(valid_choices))
            except IndexError:
                # No valid choices??
                if (len(self.hand) == 0):
                    value = random.choice(list(self.completed.keys()))
                else:
                    value = random.choice(list(self.hand.keys()))

        return Request(value)

    def respond(self,request):
        self.memory.seen(request.value)
        if request.value not in self.hand:
            return Response() # Go fish.
        else:
            cards = self.hand[request.value]
            del self.hand[request.value]
            response = Response(cards)
            return response

    def receive_response(self, response):
        if (response.card is not None):
            for card in response.card:
                self.add_card(card)
            self._update_completed()
            self.memory.remove(response.card[0].value)

    def sets(self):
        return self.completed

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

