from collections import Counter
from numpy import diff
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



def get_
