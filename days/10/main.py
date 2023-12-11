def shoelace_formula(x_coords: list[int], y_coords: list[int]) -> int:
    n = len(x_coords)
    return int(0.5 * abs(sum(x_coords[i] * y_coords[(i + 1) % n] - x_coords[(i + 1) % n] * y_coords[i] for i in range(n))))


def in_bounds(map: list[list[str]], x: int, y: int) -> bool:
    return 0 <= x < len(map) and 0 <= y < len(map[0])


def is_connecting(map: list[list[str]], x1: int, y1: int, x2: int, y2: int) -> bool:
    x_diff = x2 - x1
    y_diff = y2 - y1

    if x_diff == 1 and y_diff == 0:
        return map[x1][y1] in ['S', '|', '7', 'F'] and map[x2][y2] in ['|', 'L', 'J']
    elif x_diff == -1 and y_diff == 0:
        return map[x1][y1] in ['S', '|', 'L', 'J'] and map[x2][y2] in ['|', '7', 'F']
    elif x_diff == 0 and y_diff == 1:
        return map[x1][y1] in ['S', '-', 'F', 'L'] and map[x2][y2] in ['-', 'J', '7']
    elif x_diff == 0 and y_diff == -1:
        return map[x1][y1] in ['S', '-', '7', 'J'] and map[x2][y2] in ['-', 'F', 'L']

    return False


def get_connections(map: list[list[str]], seen: list[tuple[int, int]], x1: int, y1: int) -> list[tuple[int, int]]:
    pipe_chars = ['|', '-', 'L', 'J', '7', 'F', 'S']
    to_check = [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
    return [(x2, y2) for (x2, y2) in to_check if
            in_bounds(map, x2, y2) and map[x2][y2] in pipe_chars and (x2, y2) not in seen and is_connecting(map, x1, y1,
                                                                                                            x2, y2)]


def get_neighbouring_coords(map: list[list[str]], x: int, y: int) -> list[tuple[int, int]]:
    return [(x2, y2) for (x2, y2) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if
            in_bounds(map, x2, y2)]


if __name__ == '__main__':
    with open('input.txt') as file:
        map: list[list[str]] = [list(line.strip()) for line in file.readlines()]

    index_start: int = [i for (i, line) in enumerate(map) if 'S' in line][0]
    start: tuple[int, int] = (index_start, map[index_start].index('S'))

    seen: list[tuple[int, int]] = [start]
    positions: list[tuple[int, int]] = [start]
    steps: int = 0

    while True:
        connections: list[list[tuple[int, int]]] = [get_connections(map, seen, x, y) for (x, y) in positions]
        positions: list[tuple[int, int]] = [item for sublist in connections for item in sublist]
        steps += 1

        # We've reached the same position
        if len(set(positions)) == 1:
            seen.append(positions[0])
            break

        # Insert loop into seen in clock-wise order as shoelace formula needs vertices clockwise/anti-clockwise
        seen.append(positions[0])
        seen.insert(0, positions[1])

    area: int = shoelace_formula([x for (x, y) in seen], [y for (x, y) in seen])

    print('Part one', steps, 6640)
    # Pick's theorem gets us the area within boundaries
    print('Part two', area - steps + 1, 411)
