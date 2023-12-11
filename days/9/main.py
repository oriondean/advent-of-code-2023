def derive_sequence(sequence: list[int]) -> int:
    sequence_inner = [element - sequence[index] for index, element in enumerate(sequence[1:])]
    print('derive sequence', sequence, sequence_inner)

    if all([element == 0 for element in sequence_inner]):
        print('result', sequence_inner[0])
        return sequence[0] - sequence_inner[0]


    result = sequence[0] - derive_sequence(sequence_inner)
    print('result', result)
    return result


if __name__ == '__main__':
    with open('input.txt') as file:
        sequences = [list(map(int, line.strip().split(' '))) for line in file.readlines()]
        file.close()

    print(sequences)

    result = derive_sequence(sequences[2])

    print(result)

    print(sum([derive_sequence(sequence) for sequence in sequences]))
