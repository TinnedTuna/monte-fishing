import random

from monte_fishing.game import (
        Response,
        Request,
        )

class RandomPlayer(object):
    def __init__(self,hand):
        self.name="Basic"
        self.hand = {}
        for card in hand:
            if card.value in self.hand:
                self.hand[card.value].append(card)
            else:
                self.hand[card.value] = [card]

    def request(self):
        value = random.choice(self.hand.keys())
        return Request(value)

    def respond(self,request):
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
            if (card_value in self.hand):
                self.hand[card_value] = self.hand[card_value] + response.card
            else:
                self.hand[card_value] = response.card

    def add_card(self, card):
        if (card.value in self.hand):
            self.hand[card.value].append(card)
        else:
            self.hand[card.value] = [card]

    def sets(self):
        return self.hand 

    def __repr__(self):
        return "Basic Player{sets: "+str(len(self.sets()))+" hand: "+str(self.hand)+"}"

