from tqdm import tqdm

INPUT = "496138527"


class Cup:
    next = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value} → {self.next.value}'


initial_order = [int(x) for x in INPUT] + list(range(10, 1_000_001))
cups = {value: Cup(value) for value in initial_order}
for value, next_value in zip(initial_order, initial_order[1:] + initial_order[:1]):
    cups[value].next = cups[next_value]


current_cup = cups[initial_order[0]]
for i in tqdm(range(10_000_000)):
    to_move = [current_cup.next, current_cup.next.next, current_cup.next.next.next]
    next_cup = to_move[-1].next
    destination_value = current_cup.value - 1 if current_cup.value > 1 else max(initial_order)
    while destination_value in [cup.value for cup in to_move]:
        destination_value = destination_value - 1 if destination_value > 1 else max(initial_order)
    to_move[-1].next = cups[destination_value].next
    cups[destination_value].next = to_move[0]
    current_cup.next = next_cup
    current_cup = current_cup.next

print(cups[1].next.value * cups[1].next.next.value)
