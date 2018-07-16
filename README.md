One of the concerns about BS Poker is that the odds of different hands changes
over time and with the number of players, so perhaps we can have different
numbers of suits or different numbers of cards per suit that will allow for a
nicely balanced game at various sizes.


Approach
-------

Rather than analytically computing the odds of different hands being present
with different numbers of cards, I'm taking a simulation approach.  Basically,
the function `SimulateOne` will draw a random set of `numCards`, then check
whether each of the hands exists. This is then returned to `SimulateMany`.

