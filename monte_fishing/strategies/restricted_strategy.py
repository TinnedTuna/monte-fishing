from monte_fishing.players.restricted import RestrictedMemoryPlayer
from monte_fishing.strategy import StrategyFactory

class MemoryStrategy(StrategyFactory):
    def __init__(self):
        pass;

    def get_player(self, hand):
        return RestrictedMemoryPlayer(hand)
