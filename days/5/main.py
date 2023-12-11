from sys import maxsize


def run_chain(seeds: list[int], mappers: list[list[int]]) -> int:
    result = maxsize

    for seed in seeds:
        value = seed
        chains = mappers

        for chain in chains:
            match = [(dest, source, r) for (dest, source, r) in chain if source <= value <= source + r]
            if match:
                [dest, source, r] = match[0]
                value = (value - source) + dest

        if value < result:
            result = value

    return result


if __name__ == '__main__':
    seeds = []
    mappers: list[list[int]] = []

    with open('input.txt') as file:
        for line_raw in file:
            line = line_raw.strip()
            if line.startswith('seeds: '):
                seeds = list(map(int, line.split(': ')[1].split(' ')))
            elif line.endswith('map:'):
                mappers.append([])
            elif line:
                value: list[int] = list(map(int, line.split(' ')))
                mappers[-1].append(value)

        file.close()

    print('Part one', run_chain(seeds, mappers))

    ranges = [sorted([(s, s + r - 1, d - s) for (d, s, r) in m]) for m in mappers]
    seeds = sorted([(seeds[i - 1], seeds[i - 1] + length) for (i, length) in enumerate(seeds) if i % 2 == 1])

    # Add -maxsize and +maxsize boundaries to ranges
    for r in ranges:
        r.insert(0, (-maxsize, r[0][0] - 1, 0))
        r.append((r[-1][1], maxsize, 0))

    for map in ranges:
        new_seeds = []

        for candidate in seeds:
            matches = [r for r in map if r[0] <= candidate[1] and r[1] >= candidate[0]]
            for match in matches:
                new_seeds.append(
                    (max(candidate[0], match[0]) + match[2], min(candidate[1], match[1]) + match[2]),
                )

        seeds = new_seeds

    print('Part two', min([x for (x, y) in seeds]))
