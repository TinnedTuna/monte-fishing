import unittest

from monte_fishing.deck import Deck

class DeckTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeckCreation(self):
        d = Deck()
        self.assertTrue(len(d.deck) == 52)

    def testGetCard(self):
        d = Deck()
        self.assertTrue(d.get_card() not in d.deck)
