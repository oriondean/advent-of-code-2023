from collections import Counter
from functools import cmp_to_key


def determine_type(cards: str):
    uniques = Counter(cards)
    jokers = uniques['J']

    # if five of a kind, all good
    # if four of a kind, upgrade to five
    # if three of a kind, four a kind
    # if full house, ???

    if [(card, count) for (card, count) in uniques.items() if count == 5 or (card is not 'J' and ((count + jokers) == 5))]:
        return 7  # five of a kind
    elif [(card, count) for (card, count) in uniques.items() if count == 4 or (card is not 'J' and ((count + jokers) == 4))]:
        return 6  # four of a kind
    elif [(card, count) for (card, count) in uniques.items() if count == 3 or (card is not 'J' and ((count + jokers) == 3))]:
        uniques_no_joker = len(uniques) - (1 if jokers else 0)

        print(cards, 5 if uniques_no_joker == 2 else 4)
        return 5 if uniques_no_joker == 2 else 4  # full house or three of a kind
    elif sorted([count for count in uniques.values()]) == [1, 2, 2]:
        return 3  # two pair
    elif max([count for count in uniques.values()]) == 2:
        return 3 if jokers else 2  # one pair
    else:
        return 2 if jokers else 1  # high card


def parse_hand(line):
    [cards, bid] = line.strip().split(' ')
    return list(cards), int(bid), determine_type(cards)


def compare_hand(a, b):
    if a[2] != b[2]:
        return a[2] - b[2]
    else:
        return rankings.index(a[0][0]) - rankings.index(b[0][0]) or rankings.index(a[0][1]) - rankings.index(b[0][1]) or \
            rankings.index(a[0][2]) - rankings.index(b[0][2]) or rankings.index(a[0][3]) - rankings.index(b[0][3]) or \
            rankings.index(a[0][4]) - rankings.index(b[0][4])


if __name__ == '__main__':
    rankings = list(reversed(['A', 'K', 'Q', 'T', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']))
    with open('input.txt') as file:
        input = [parse_hand(line) for line in file.readlines()]
        file.close()

    sorty = sorted(input, key=cmp_to_key(compare_hand))
    print(sorty)

    print([h[1] * (i + 1) for i, h in enumerate(sorty)])
    print('Part one', sum([h[1] * (i + 1) for i, h in enumerate(sorty)]))  # 249638405
    # 249776650 right