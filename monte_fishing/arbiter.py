import multiprocessing
import straight.plugin

from monte_fishing.game import Game

class Arbiter(multiprocessing.Process):
    """Arbiter of multiple games. Loads plugins, and runs the games.
    """
    def __init__(self,trials):
        self.strategies=straight.plugin.load('monte_fishing.strategies')
        self.trials = trials
        self.outcome_log = []

    def run(self):
        """Runs each strategy against each other strategy for however many 
           trials was requested. In general, takes O(trials*|strategies|) time.
        """
        for i in range(self.trials):
            self._trial()
        return self.outcome_log
    
    def _trial(self):
        for strategy_one in self.strategies:
            for strategy_two in self.strategies:
                g = Game(strategy_one, strategy_two)
                outcome = g.run()
                self.outcome_log.append(outcome)
                print(outcome)

