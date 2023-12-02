from functools import reduce


def parse_round(memo: tuple[int, int, int, bool], subround: str) -> tuple[int, int, int, bool]:
    value = int(subround.strip().split(' ')[0])
    if subround.endswith('red'):
        return value, memo[1], memo[2], memo[3] and value <= 12
    elif subround.endswith('green'):
        return memo[0], value, memo[2], memo[3] and value <= 13
    return memo[0], memo[1], value, memo[3] and value <= 14


if __name__ == '__main__':
    result_one = 0
    result_two = 0
    index = 0

    with open('input.txt') as file:
        for line in file:
            rounds_raw = [round.split(', ') for round in line.strip().split(': ')[1].split(';')]
            rounds = [reduce(parse_round, round, (0, 0, 0, True)) for round in rounds_raw]

            if all([x[3] for x in rounds]):
                result_one += (index + 1)
            result_two += max([x[0] for x in rounds]) * max([x[1] for x in rounds]) * max([x[2] for x in rounds])
            index += 1
    file.close()

    print('Part one', result_one, 2913)
    print('Part two', result_two, 55593)
