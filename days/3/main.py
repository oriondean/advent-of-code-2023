def extract_numbers(chars: list[str], index: int) -> list[list[(int, int)]]:
    result: list[list[(int, int)]] = []
    digits: list[(int, int)] = []

    for i, char in enumerate(chars):
        if char.isdigit():
            digits.append((index, i))
        else:
            if len(digits):
                result.append(digits)
                digits = []

    if len(digits):
        result.append(digits)

    return result


def get_adjacent_coords(digits: list[(int, int)], width: int, height: int) -> list[(int, int)]:
    coords = []

    for i, coord in enumerate(digits):
        adjacent = []

        if i == 0:
            adjacent += [(coord[0] - 1, coord[1] - 1), (coord[0], coord[1] - 1), (coord[0] + 1, coord[1] - 1)]
        if i == len(digits) - 1:
            adjacent += [(coord[0] - 1, coord[1] + 1), (coord[0], coord[1] + 1), (coord[0] + 1, coord[1] + 1)]
        adjacent += [(coord[0] - 1, coord[1]), (coord[0] + 1, coord[1])]

        coords += [(x, y) for (x, y) in adjacent if -1 < x < height and -1 < y < width]

    return coords


if __name__ == '__main__':
    index = 0
    schematic = []
    numbers = []

    with open('input.txt') as file:
        for line_raw in file:
            chars = list(line_raw.strip())
            schematic.append(chars)
            numbers += extract_numbers(chars, index)
            index += 1

    width = len(schematic[0])
    height = len(schematic)
    gears = dict()
    result_one = 0

    for digits in numbers:
        coords = get_adjacent_coords(digits, width, height)
        gear_coords = [(x, y) for (x, y) in coords if schematic[x][y] == '*']

        if [(x, y) for (x, y) in coords if schematic[x][y] == '*']:
            number = int(''.join([schematic[x][y] for (x, y) in digits]))
            key = str(gear_coords[0][0]) + ',' + str(gear_coords[0][1])

            if key in gears:
                gears[key].append(number)
            else:
                gears[key] = [number]

        if [(x, y) for (x, y) in coords if schematic[x][y] != '.']:
            result_one += int(''.join([schematic[x][y] for (x, y) in digits]))

    print('Part one', result_one)
    print('Part two', sum([x[0] * x[1] for x in gears.values() if len(x) == 2]))
