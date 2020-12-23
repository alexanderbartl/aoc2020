from collections import deque

INPUT = "496138527"

cups = deque(int(x) for x in INPUT)
for _ in range(100):
    current_cup = cups.popleft()
    cups.append(current_cup)
    three_cups = (cups.popleft(), cups.popleft(), cups.popleft())
    try:
        destination = cups.index(max(cup for cup in cups if cup < cups[-1])) + 1
    except ValueError:
        destination = cups.index(max(cups)) + 1
    for cup in three_cups[::-1]:
        cups.insert(destination, cup)

    print(cups)

cups.rotate(-cups.index(1))
print(''.join(map(str, cups))[1:])
