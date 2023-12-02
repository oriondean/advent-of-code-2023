import re

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers_pattern = re.compile('$|'.join(numbers) + '$')


def find_digit(text: str, is_reverse: bool) -> str:
    r = range(0, len(text), 1)
    if is_reverse:
        r = reversed(r)

    for index in r:
        if text[index].isdigit():
            return text[index]

        match = re.search(numbers_pattern, text[:index + 1])
        if match:
            return str(numbers.index(match.group()) + 1)


if __name__ == '__main__':
    sum_one: int = 0
    sum_two: int = 0

    with open('input.txt') as file:
        for line in file:
            digits: list[str] = [d for d in line if d.isdigit()]
            sum_one += int(digits[0] + digits[-1])
            sum_two += (int(find_digit(line, False) + find_digit(line, True)))
        file.close()

    print('Part one', sum_one)
    print('Part two', sum_two)
