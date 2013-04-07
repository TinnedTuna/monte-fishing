Monte Fishing
=============

Monte Fishing is a small Python framework for playing various Go Fish! 
strategies against one-another to try to determine which is best.

It simply plays every strategy against every other strategy many thousands of 
times, with different starting decks.


Installing and Running
======================

  $> vitualenv env
  $> ./env/bin/python setup.py install
  $> ./env/bin/python -m monte_fishing.main --trials <trials> --processes <processes>

Creating your own Strategy
==========================

This is actually very simple, but you must note that the framework **does not 
enforce rules**, your strategy must simply play by the rules for a reasonable 
results.

It is probably easiest if you simply clone the basic player, 
monte_fishing/players/basic.py into your new player and re-code the various 
methods. You must then write a simple strategy factory. You can usually get 
away with cloning the default factory, found in 
monte_fishing/strategies/basic_strategy.py. Your new players and strategies 
must reside in the same directories as the other players and strategies.




