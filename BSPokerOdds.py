from __future__ import print_function
#from sys import stderr
from collections import Counter
from numpy import diff, zeros, arange, argsort
from numpy.random import shuffle


def Pair(cards, cardCounts, cardsPerSuit):
    return cardCounts.most_common(1)[0][1] >= 2

def TwoPair(cards, cardCounts, cardsPerSuit):
    most_common = cardCounts.most_common(2)
    return len(most_common) > 1 and most_common[1][1] >= 2

def ThreeOfAKind(cards, cardCounts, cardsPerSuit):
    return cardCounts.most_common(1)[0][1] >= 3

def Straight(cards, cardCounts, cardsPerSuit):
    run = 1
    for i in diff(sorted([card % cardsPerSuit for card in cards])):
        if i == 1:
            run += 1
        elif i > 1:
            # A pair doesn't invalidate a straight.
            # Example: 3,4,5,5,6,7 is fine.
            run = 1
        if run >= 5:
            return True
    return False

def Flush(cards, cardCounts, cardsPerSuit):
    suit_counts = Counter(card // cardsPerSuit for card in cards)
    return suit_counts.most_common(1)[0][1] >= 5

def FullHouse(cards, cardCounts, cardsPerSuit):
    most_common = cardCounts.most_common(2)
    return ((len(most_common) > 1) and
            (most_common[0][1] >= 3 and most_common[1][1] >= 2))

def FourOfAKind(cards, cardCounts, cardsPerSuit):
    return cardCounts.most_common(1)[0][1] >= 4

def FiveOfAKind(cards, cardCounts, cardsPerSuit):
    return cardCounts.most_common(1)[0][1] >= 5

def StraightFlush(cards, cardCounts, cardsPerSuit):
    if Flush(cards, cardCounts, cardsPerSuit):
        run = 1
        for i in diff(cards):
            if i % cardsPerSuit == 0:
                run = 1
            elif i == 1:
                run += 1
            else:
                run = 1
            if run >= 5:
                return True
    return False

check_hands = [
    FiveOfAKind,
    StraightFlush,
    FourOfAKind,
    FullHouse,
    Flush,
    Straight,
    ThreeOfAKind,
    TwoPair,
    Pair,
]

def SimulateOne(cardsPerSuit, numSuits, numCards, verbose=False):
    res = zeros(len(check_hands), dtype=int)
    deck = arange(cardsPerSuit * numSuits)
    shuffle(deck)
    cards = sorted(deck[:numCards])
    cardCounts = Counter(card % cardsPerSuit for card in cards)
    for i, func in enumerate(check_hands):
        res[i] = func(cards, cardCounts, cardsPerSuit)
    if verbose:
        print(['{}{}'.format(i % cardsPerSuit+1, chr(ord('A')+i//cardsPerSuit))
               for i in sorted(cards)])
    return res

def SimulateMany(cardsPerSuit, numSuits, numCards, iterations):
    res = zeros(len(check_hands), dtype=int)
    for i in range(int(iterations)):
        res += SimulateOne(cardsPerSuit, numSuits, numCards)
    return res/iterations


def AverageBadness(cardsPerSuit, numSuits, minPerPlayer, maxPerPlayer,
                   numPlayers, iterations=1e4):
    badness = 0
    n = 0
    expected_order = arange(len(check_hands))
    for i in range(minPerPlayer * numPlayers, maxPerPlayer*numPlayers+1):
        probs = SimulateMany(cardsPerSuit, numSuits, i, iterations)
        badness += ((argsort(probs) - expected_order)**2).sum()
        n += 1
        print(i, badness)
    return badness/n



