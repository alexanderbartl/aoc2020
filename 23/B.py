from collections import deque
from tqdm import tqdm

INPUT = "496138527"


def get_destination_index(number):
    try:
        return cups.index(number) + 1
    except ValueError:
        return None


cups = deque([int(x) for x in INPUT] + list(range(10, 1_000_001)))
for _ in tqdm(range(10_000_000)):
    current_cup = cups.popleft()
    cups.append(current_cup)
    three_cups = (cups.popleft(), cups.popleft(), cups.popleft())
    try:
        destination = get_destination_index(current_cup - 1) or \
                  get_destination_index(max(cup for cup in cups if cup < cups[-1])) or \
                  get_destination_index(max(cups))
    except ValueError:
        destination = get_destination_index(max(cups))
    for cup in three_cups[::-1]:
        cups.insert(destination, cup)

cups.rotate(-cups.index(1))
print(cups[1] * cups[2])
