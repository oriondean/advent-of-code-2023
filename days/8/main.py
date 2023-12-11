from math import gcd


def lowest_common_multiple(*args: list[int]) -> int:
    result = args[0]
    for num in args[1:]:
        result = abs(result * num) // gcd(result, num)
    return result


def navigate(positions: list[str], instructions: str) -> list[int]:
    index_instruction: int = 0
    step_count: int = 1
    result: list[int] = []

    while any([not position.endswith('Z') for position in positions]):
        instruction = instructions[index_instruction]

        for index_position, position in enumerate(positions):
            if not position.endswith('Z'):
                positions[index_position] = nodes[position][0 if instruction == 'L' else 1]

                if positions[index_position].endswith('Z'):
                    result.append(step_count)

        index_instruction = (index_instruction + 1) % len(instructions)
        step_count += 1

    return result


if __name__ == '__main__':
    with open('input.txt') as file:
        input: list[str] = [line.strip() for line in file.readlines()]
        file.close()

    nodes: dict[str, list[str]] = {}
    for p in [i.split(' = ') for i in input[2:]]:
        nodes[p[0]] = p[1][1: -1].split(', ')

    positions: list[str] = [key for key in nodes.keys() if key.endswith('A')]

    print('Part one', navigate(['AAA'], input[0])[0])
    print('Part two', lowest_common_multiple(*navigate(positions, input[0])), 17099847107071)
