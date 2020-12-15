INPUT = [18, 11, 9, 0, 5, 1]

last_seen = {number: index + 1 for index, number in enumerate(INPUT[:-1])}
turn = len(INPUT)
number = INPUT[-1]

while turn < 30_000_000:
    previous_number = number
    number = turn - last_seen[previous_number] if previous_number in last_seen else 0
    last_seen[previous_number] = turn
    turn += 1
    if turn == 2020:
        print(number)

print(number)
