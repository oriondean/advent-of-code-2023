from functools import reduce

if __name__ == '__main__':
    with open('input.txt') as file:
        input = file.readlines()
        file.close()

    times_raw = input[0].split(': ')[1].strip()
    times = [int(time) for time in times_raw.split(' ') if time.isdigit()]
    times.append(int(times_raw.replace(' ', '')))

    distances_raw = input[1].split(': ')[1].strip()
    distances = [int(distance) for distance in distances_raw.split(' ') if distance.isdigit()]
    distances.append(int(distances_raw.replace(' ', '')))

    result = []
    for race in range(0, len(times)):
        hold_time = 1
        while (hold_time * (times[race] - hold_time)) <= distances[race]:
            hold_time += 1
        result.append(times[race] - (hold_time * 2) + 1)

    print('Part one', reduce((lambda x, y: x * y), result[0:-1]))
    print('Part two', result[-1])
