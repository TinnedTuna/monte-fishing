import multiprocessing
import sys
import straight.plugin

from monte_fishing.game import Game
from monte_fishing.strategy import StrategyFactory

class Arbiter(multiprocessing.Process):
    """Arbiter of multiple games. Loads plugins, and runs the games.
    """
    def __init__(self,trials,print_lock):
        multiprocessing.Process.__init__(self)
        print("About to load strategies")
        self.strategies=straight.plugin.load('monte_fishing.strategies', subclasses=StrategyFactory).produce()
        if (len(self.strategies) == 0):
            print("no plugins loaded.")
        for s in self.strategies:
            print(s)
        self.trials = trials
        self.print_lock = print_lock
        self.outcome_log = []

    def run(self):
        """Runs each strategy against each other strategy for however many 
           trials was requested. In general, takes O(trials*|strategies|^2) time.
        """
        for i in range(self.trials):
            self._trial()
    
    def _trial(self):
        for strategy_one in self.strategies:
            for strategy_two in self.strategies:
                g = Game(strategy_one, strategy_two)
                outcome = g.run()
                self.print_lock.acquire()
                print(outcome)
                sys.stdout.flush()
                self.print_lock.release()
