from collections import Counter
from functools import cmp_to_key


def determine_type(cards: str, count_jokers: bool) -> int:
    uniques = Counter(cards)
    jokers = uniques['J'] if count_jokers else 0

    if [(card, count) for (card, count) in uniques.items() if
        count == 5 or (card != 'J' and ((count + jokers) == 5))]:
        return 7  # five of a kind
    elif [(card, count) for (card, count) in uniques.items() if
          count == 4 or (card != 'J' and ((count + jokers) == 4))]:
        return 6  # four of a kind
    elif [(card, count) for (card, count) in uniques.items() if
          count == 3 or (card != 'J' and ((count + jokers) == 3))]:
        uniques_no_joker = len(uniques) - (1 if jokers else 0)
        return 5 if uniques_no_joker == 2 else 4  # full house or three of a kind
    elif sorted([count for count in uniques.values()]) == [1, 2, 2]:
        return 3  # two pair
    elif max([count for count in uniques.values()]) == 2:
        return 3 if jokers else 2  # one pair
    else:
        return 2 if jokers else 1  # high card


def parse_hand(line: str, count_jokers: bool) -> tuple[list[str], int, int]:
    [cards, bid] = line.strip().split(' ')
    return list(cards), int(bid), determine_type(cards, count_jokers)


def compare_hand(a: tuple[list[str], int, int], b: tuple[list[str], int, int]):
    if a[2] != b[2]:
        return a[2] - b[2]
    else:
        return rank.index(a[0][0]) - rank.index(b[0][0]) or rank.index(a[0][1]) - rank.index(b[0][1]) or \
            rank.index(a[0][2]) - rank.index(b[0][2]) or rank.index(a[0][3]) - rank.index(b[0][3]) or \
            rank.index(a[0][4]) - rank.index(b[0][4])


if __name__ == '__main__':
    with open('input.txt') as file:
        input = file.readlines()
        file.close()

    rank = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))
    cards = sorted([parse_hand(line, False) for line in input], key=cmp_to_key(compare_hand))
    print('Part one', sum([h[1] * (i + 1) for i, h in enumerate(cards)]))

    rank = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']))
    cards = sorted([parse_hand(line, True) for line in input], key=cmp_to_key(compare_hand))
    print('Part two', sum([h[1] * (i + 1) for i, h in enumerate(cards)]))
