from numpy import rot90
from heapq import heappop, heappush


def dijkstra(graph: dict[str, dict[str, int]], start: str) -> dict[str, float]:
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heappush(priority_queue, (distance, neighbour))

    return distances


def expand(map: list[list[str]]) -> list[list[str]]:
    map_expanded: list[list[str]] = []

    for row in range(0, len(map)):
        if all([c == '.' for c in map[row]]):
            map_expanded.append(map[row])

        map_expanded.append(map[row])

    return map_expanded


def get_distance(x1: int, y1: int, x2: int, y2: int, row_indexes: list[int], col_indexes: list[int],
                 expand_distance: int) -> int:
    row_overlap = [c for c in row_indexes if min(x1, x2) < c < max(x1, x2)]
    col_overlap = [c for c in col_indexes if min(y1, y2) < c < max(y1, y2)]
    return abs(x2 - x1) + abs(y2 - y1) + (len(row_overlap) * (expand_distance - 1)) + (
            len(col_overlap) * (expand_distance - 1))


def parse_galaxies(map) -> list[tuple[int, int]]:
    galaxies = []
    for row in range(0, len(map)):
        for col in range(0, len(map[0])):
            if map[row][col] == '#':
                galaxies.append((row, col))
    return galaxies


def calculate_distances(galaxies: list[tuple[int, int]], row_indexes: list[int], column_indexes: list[int],
                        expand_distance: int) -> dict[str, dict[str, int]]:
    result: dict[str, dict[str, int]] = {}

    for index, galaxy in enumerate(galaxies):
        result[str(galaxy)] = {}

        for other in galaxies:
            distance = get_distance(galaxy[0], galaxy[1], other[0], other[1], row_indexes, column_indexes,
                                    expand_distance)
            result[str(galaxy)].update({str(other): distance})

    return result


if __name__ == '__main__':
    with open('input.txt') as file:
        map: list[list[str]] = [list(line.strip()) for line in file.readlines()]

    row_indexes: list[int] = [i for (i, row) in enumerate(map) if all([c == '.' for c in row])]
    column_indexes: list[int] = [i for (i, row) in enumerate(rot90(map, k=-1)) if all([c == '.' for c in row])]
    galaxies: list[tuple[int, int]] = parse_galaxies(map)

    graph = calculate_distances(galaxies, row_indexes, column_indexes, 2)
    result = sum([sum(list(dijkstra(graph, str(galaxy)).values())) for galaxy in galaxies]) // 2
    print('part one', result)

    graph = calculate_distances(galaxies, row_indexes, column_indexes, 1000000)
    result = sum([sum(list(dijkstra(graph, str(galaxy)).values())) for galaxy in galaxies]) // 2
    print('part two', result)
