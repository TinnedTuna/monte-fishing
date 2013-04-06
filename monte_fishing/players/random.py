import random

from monte_fishing.game import (
        Response,
        Request,
        )

class RandomPlayer():
    def __init__(self,hand):
        self.hand = hand

    def request(self):
        return Request(random.choice(self.hand))

    def respond(self,request):
        if request.get_card() not in self.hand:
            return Response() # Go fish.
        else:
            self.hand.remove(request.get_card())
            return Response(request.get_card())

    def receive_response(self, response):
        self.hand.append(response.get_card())



