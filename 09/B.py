with open('input.txt') as f:
    numbers = [int(n) for n in f.readlines()]

target = 22477624


def find_continuous_set(start):
    running_sum = 0
    idx = start
    while running_sum < target:
        running_sum += numbers[idx]
        idx += 1

    if running_sum == target:
        return min(numbers[start:idx + 1]), max(numbers[start:idx + 1])

    return None


for i in range(25, 1000):
    solution = find_continuous_set(i)
    if solution is not None:
        print(solution[0] + solution[1])
        break

