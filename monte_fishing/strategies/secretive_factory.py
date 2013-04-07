from monte_fishing.players.secretive import SecretivePlayer
from monte_fishing.strategy import StrategyFactory

class SecretiveStrategy(StrategyFactory):
    def __init__(self):
        pass;

    def get_player(self, hand):
        return SecretivePlayer(hand)
