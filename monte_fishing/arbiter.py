import multiprocessing
import straight.plugin

from monte_fishing.game import Game
from monte_fishing.strategy import StrategyFactory

class Arbiter(multiprocessing.Process):
    """Arbiter of multiple games. Loads plugins, and runs the games.
    """
    def __init__(self,trials,printer):
        multiprocessing.Process.__init__(self)
        printer.print_synchronised("About to load strategies")
        self.strategies=straight.plugin.load('monte_fishing.strategies', subclasses=StrategyFactory).produce()
        if (len(self.strategies) == 0):
            printer.print_synchronised("no plugins loaded.")
        for s in self.strategies:
            printer.print_synchronised(s)
        self.trials = trials
        self.printer = printer
        self.outcome_log = []

    def run(self):
        """Runs each strategy against each other strategy for however many 
           trials was requested. In general, takes O(trials*|strategies|^2) time.
        """
        for i in range(self.trials):
            self._trial()
        self.printer.print_batch(self.outcome_log)
    
    def _trial(self):
        count = 0;
        for strategy_one in self.strategies:
            for strategy_two in self.strategies:
                g = Game(strategy_one, strategy_two)
                outcome = g.run()
                self.outcome_log.append(str(outcome))
                if len(self.outcome_log) > 50:
                    self.printer.print_batch(self.outcome_log)
                    self.outcome_log=[]
