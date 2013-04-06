from monte_fishing.deck import Deck

class Response():
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
        self.card = card

    def __eq__(self,other):
        if (other.go_fish == self.go_fish):
            return True
        else:
           return (other.card == self.card)

class Request():
    """Encapsulate's a player's request for a card.
    """
    def __init__(self, card=None):
        self.card = card

    def __eq__(self, other):
        return (other.card == self.card)

class Outcome():
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

class Game():
    """Conducts a game between two players.
    """
    def __init__(self, player_one_factory, player_two_factory):
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
        resp = p2.respond(req)
        while (resp != self.go_fish):
          p1.receive_response(resp)
          req = p1.request()
          resp = p2.respond(req)
        resp.set_card(self.deck.get_card())
        p1.receive_response(resp)

    def _outcome():
        p1_sets = self.player_one.sets()
        p2_sets = self.player_two.sets()
        return Outcome(self.player_one, self.player_two)
       
    def run(self):
        """Runs the game by allowing the players to take turns against one
           another.
        """
        while (True):
            try: 
                self._take_turn(self.player_one, self.player_two);
            except DeckEmptyError:
                return
            try: 
                self._take_turn(self.player_two, self.player_one);
            except DeckEmptyError:
                return
        return self._outcome()
