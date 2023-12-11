def derive_sequence(sequence: list[int], extrapolate_forwards: bool) -> int:
    sequence_inner = [element - sequence[index] for index, element in enumerate(sequence[1:])]

    if all([element == 0 for element in sequence_inner]):
        if extrapolate_forwards:
            return sequence[-1] + sequence_inner[0]
        return sequence[0] - sequence_inner[-1]

    if extrapolate_forwards:
        return sequence[-1] + derive_sequence(sequence_inner, extrapolate_forwards)
    else:
        return sequence[0] - derive_sequence(sequence_inner, extrapolate_forwards)


if __name__ == '__main__':
    with open('input.txt') as file:
        sequences = [list(map(int, line.strip().split(' '))) for line in file.readlines()]
        file.close()

    print('Part one', sum([derive_sequence(sequence, True) for sequence in sequences]))
    print('Part two', sum([derive_sequence(sequence, False) for sequence in sequences]))

