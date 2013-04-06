from monte_fishing.players.random_player import RandomPlayer
from monte_fishing.strategy_factory import StrategyFactory

class RandomStrategy(StrategyFactory):
    def __init__(self):
        pass;

    def get_player(self, hand):
        return RandomPlayer(hand)
