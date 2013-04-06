from monte_fishing.players.memory import MemoryPlayer
from monte_fishing.strategy import StrategyFactory

class RandomStrategy(StrategyFactory):
    def __init__(self):
        pass;

    def get_player(self, hand):
        return MemoryPlayer(hand)
