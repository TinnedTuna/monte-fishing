from monte_fishing.deck import (
        Deck,
        DeckEmptyError,
        )

class Response(object):
    """Encapsulates an opponent's response to a request.
    """
    def __init__(self, card=None):
        if (card is None):
            self.go_fish = True
            self.card = None
        else: 
            self.go_fish = False
            self.card = card

    def set_card(self, card):
        self.card = [card]

    def __eq__(self,other):
        if (other.go_fish == self.go_fish):
            return True
        else:
           return (other.card == self.card)

    def __repr__(self):
        if (self.card is None):
            card = "None"
        else:
            card = str(self.card)
        return "Response{go_fish:"+str(self.go_fish)+" card:"+card+"}"

class Request(object):
    """Encapsulate's a player's request for a card.
    """
    def __init__(self, value=None):
        self.value = value

    def __eq__(self, other):
        return (other.value == self.value)

    def __repr__(self):
        return "Request{value: "+str(self.value)+"}"

class Outcome(object):
    """Determines the winner of a game between two players.
    """
    def __init__(self, p1, p2):
        assert p1 is not None
        assert p2 is not None
        if (len(p1.sets()) > len(p2.sets())):
            self.winner = p1 
            self.loser = p2
        elif (len(p2.sets()) > len(p1.sets())):
            self.winner = p2
            self.loser = p1
        else:
            self.winner = None
            self.loser = None

    def get_winning_strategy(self):
        if (self.winner is not None):
            return self.winner.get_strategy_name()
        else:
            return None

    def get_loser_strategy(self):
        if (self.loser is not None):
            return self.loser.get_strategy_name()
        else:
            return None

    def __repr__(self):
        return "Outcome{winner: "+str(self.winner)+" loser:"+str(self.loser)+"}"

class Game(object):
    """Conducts a game between two players.
    """
    def __init__(self, strategy_one_factory, strategy_two_factory):
        self.deck = Deck()
        self.go_fish = Response()
        self.player_one = strategy_one_factory.get_player(self.deck.get_hand(7)) 
        self.player_two = strategy_two_factory.get_player(self.deck.get_hand(7)) 

    def _take_turn(self, p1, p2):
        """Allows p1 to make a guess against p2.

        In the event that p1's guess is correct, it gets to see p2's response 
        and continue guessing.
        """
        req = p1.request()
        print("p1 request: {}".format(str(req)))
        resp = p2.respond(req)
        print("p2 response: {}".format(str(resp)))
        while (not resp.go_fish):
            print("p1 guessed right!")
            p1.receive_response(resp)
            req = p1.request()
            print("p1 request: {}".format(str(req)))
            resp = p2.respond(req)
            print("p2 response: {}".format(str(resp)))
        next_card = self.deck.get_card()
        print("Go fish! giving p1 new card: {}.".format(str(next_card)))
        resp.set_card(next_card)
        p1.receive_response(resp)

    def _outcome(self):
        p1_sets = self.player_one.sets()
        p2_sets = self.player_two.sets()
        return Outcome(self.player_one, self.player_two)
       
    def run(self):
        """Runs the game by allowing the players to take turns against one
           another.
        """
        try:
            while (True):
                 print("Hands: "+str(self.player_one.hand)+" \n "+str(self.player_two.hand))
                 self._take_turn(self.player_one, self.player_two);
                 self._take_turn(self.player_two, self.player_one);
        except DeckEmptyError:
            return self._outcome()
        return self._outcome()
