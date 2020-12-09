from itertools import combinations

with open('input.txt') as f:
    numbers = [int(n) for n in f.readlines()]


def is_valid(idx):
    for pair in combinations(numbers[idx - 25:idx], 2):
        if pair[0] + pair[1] == numbers[idx]:
            return True
    return False


for i in range(25, 1000):
    if not is_valid(i):
        print(numbers[i])
        break
