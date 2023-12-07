import functools
from collections import Counter

rules = {
    "J": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14
}


def mycmp(a, b):
    for x, y in zip(a, b):
        if rules[x] > rules[y]:
            return 1
        elif rules[x] < rules[y]:
            return -1
    return 0


def camel_cards():
    hands = [tuple(x.strip().split(" ")) for x in open('input.txt')]

    pairs = {x: y for x, y in hands}

    groups = {
        "five-equal": [],
        "four-equal": [],
        "full-house": [],
        "three-equal": [],
        "two-pair": [],
        "one-pair": [],
        "high-card": []
    }

    # Pair the hands in their group
    for hand, _ in hands:

        c = Counter(hand)
        num_jokers = c['J']
        del (c['J'])

        if num_jokers == 5:
            values = [5]
        else:
            char, freq = c.most_common(1)[0]
            c[char] += num_jokers

            values = list(c.values())

        if 5 in values:  # five-qual
            groups["five-equal"].append(hand)
        elif 4 in values:  # four-equal
            groups["four-equal"].append(hand)
        elif 3 in values and 2 in values:  # four-equal
            groups["full-house"].append(hand)
        elif 3 in values:  # three-equal
            groups["three-equal"].append(hand)
        elif values.count(2) == 2:  # two-pair
            groups["two-pair"].append(hand)
        elif 2 in values:  # one-pair
            groups["one-pair"].append(hand)
        else:  # high-card
            groups["high-card"].append(hand)

    # Sort each group
    for key, values in groups.items():
        groups[key] = list(sorted(values, key=functools.cmp_to_key(mycmp)))

    ranks = []
    ranks.extend(groups["high-card"])
    ranks.extend(groups["one-pair"])
    ranks.extend(groups["two-pair"])
    ranks.extend(groups["three-equal"])
    ranks.extend(groups["full-house"])
    ranks.extend(groups["four-equal"])
    ranks.extend(groups["five-equal"])

    total = 0
    for i, hand in enumerate(ranks):
        total += (i + 1) * int(pairs[hand])

    print(total)


camel_cards()
