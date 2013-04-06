from monte_fishing.players.basic import RandomPlayer
from monte_fishing.strategy import StrategyFactory

class RandomStrategy(StrategyFactory):
    def __init__(self):
        pass;

    def get_player(self, hand):
        return RandomPlayer(hand)
