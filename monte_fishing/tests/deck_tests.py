import unittest

from monte_fishing.deck import (
      Deck,
      Card,
      )

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.d = Deck()
        
    def tearDown(self):
        pass

    def testDeckCreation(self):
        self.assertEqual(len(self.d.deck), 52)

    def testGetCardDeckSize(self):
        self.assertEqual(len(self.d.deck), 52)
        c = self.d.get_card()
        self.assertEqual(len(self.d.deck), 51)

    def testGetCard(self):
        self.assertEqual(len(self.d.deck), 52)
        self.assertTrue(self.d.get_card() not in self.d.deck)
   
    def testGetHand(self):
        hand = self.d.get_hand(7)
        self.assertTrue(len(hand), 6)
       
    def testGetHandNoDuplicates(self):
        hand = self.d.get_hand(52)
        no_dupes_hand = set(hand)
        self.assertTrue(len(no_dupes_hand), 52)
        


class CardTests(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def testEquality(self):
        c_one = Card('Hearts',1)
        c_two = Card('Hearts',1)
        self.assertEqual(c_one, c_two)

    def testDisequal(self):
        c_one = Card('Hearts',1)
        c_two = Card('Hearts',2)
        self.assertNotEqual(c_one, c_two)
