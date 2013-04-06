import unittest

from monte_fishing.deck import Card

from monte_fishing.game import (
      Outcome,
      Response,
      )

class OutcomeTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWinningVLosing(self):
        winner = WinningPlayer()
        loser = LosingPlayer()
        o = Outcome(winner, loser)        
        self.assertEqual("Winning Strategy", o.get_winning_strategy())

    def testLosingDraw(self):
        o = Outcome(LosingPlayer(), LosingPlayer())
        self.assertTrue(o.get_winning_strategy() is None)

    def testWinningDraw(self):
        o = Outcome(WinningPlayer(), WinningPlayer())
        self.assertTrue(o.get_winning_strategy() is None)

    def testLosingVWinning(self):
        o = Outcome(LosingPlayer(), WinningPlayer())
        self.assertEqual("Winning Strategy", o.get_winning_strategy())


class ResponseTests(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def testGoFish(self):
        go_fish = Response()
        self.assertEqual(go_fish, Response())
        self.assertTrue(go_fish.card is None)

    def testRespondWithCard(self):
        go_fish = Response()
        player_response = Response(Card("Hearts",2))
        self.assertNotEqual(go_fish,player_response)
        self.assertEqual(player_response.card, Card("Hearts",2))
        

class LosingPlayer():
    def get_strategy_name(self):
        return "Losing Strategy"

    def sets(self):
        return []

class WinningPlayer():
    def __init__(self):
        self.won_sets = []
        for value in range(1,14):
            current_set = []
            for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
                 current_set.append(Card(suit, value))
            self.won_sets.append(current_set)
        assert self.won_sets is not None

    def get_strategy_name(self):
        return "Winning Strategy"

    def sets(self):
        assert self.won_sets is not None
        return self.won_sets
