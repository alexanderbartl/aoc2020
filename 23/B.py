from collections import deque
from tqdm import tqdm

INPUT = "496138527"
CACHE_EVERY = 1000


cups = deque([int(x) for x in INPUT] + list(range(10, 1_000_001)))
last_seen = {}
for i in tqdm(range(10_000_000)):
    if i % CACHE_EVERY == 0:
        last_seen = {number: pos for pos, number in enumerate(cups)}
    current_cup = cups.popleft()
    cups.append(current_cup)
    last_seen[current_cup] = len(cups)
    three_cups = (cups.popleft(), cups.popleft(), cups.popleft())
    for j in range(1, 5):
        destination_cup = current_cup - j if current_cup > j else current_cup - j + max(cups)
        if destination_cup not in three_cups:
            try:
                destination = cups.index(destination_cup, last_seen[destination_cup] - 100, last_seen[destination_cup]) + 1
            except ValueError:
                destination = cups.index(destination_cup, max(0, last_seen[destination_cup] - 4 * (i % CACHE_EVERY) - 10), last_seen[destination_cup]) + 1
            break

    for cup in three_cups[::-1]:
        cups.insert(destination, cup)
        last_seen[cup] = destination

cups.rotate(-cups.index(1))
print(cups[1] * cups[2])
