if __name__ == '__main__':
    scratchcards: list[(int, list[int], list[int], set[int])] = list()
    scratchcard_counts: dict[int, int] = dict()

    with open('input.txt') as file:
        for line_raw in file:
            line: list[str] = line_raw.strip().split(': ')
            id: int = int(line[0].split(' ')[-1])
            scratchcard_counts.setdefault(id, 1)

            numbers: list[str] = line[1].split(' | ')
            numbers_winning: set[int] = set([int(n) for n in numbers[0].split(' ') if n.isdigit()])
            numbers_picked: set[int] = set([int(n) for n in numbers[1].split(' ') if n.isdigit()])
            numbers_matched: set[int] = numbers_winning.intersection(numbers_picked)

            if numbers_matched:
                scratchcards.append((id, numbers_winning, numbers_picked, numbers_matched))

                for _ in range(0, scratchcard_counts.get(id, 1)):
                    for dupe in [id + x + 1 for x, _ in enumerate(numbers_matched)]:
                        scratchcard_counts.setdefault(dupe, 1)
                        scratchcard_counts[dupe] += 1

    print('Part one', sum([2 ** (len(card[3]) - 1) for card in scratchcards]))
    print('Part two', sum(scratchcard_counts.values()))
