with open('input.txt') as f:
    passes = f.readlines()


def seat_id(boarding_pass):
    row_binary = boarding_pass[:7].replace('F', '0').replace('B', '1')
    seat_binary = boarding_pass[7:].replace('L', '0').replace('R', '1')
    return int(row_binary, 2) * 8 + int(seat_binary, 2)


ids = set([seat_id(p) for p in passes])

# A
print(max(ids))

# B
for id in ids:
    if id + 1 not in ids and id + 2 in ids:
        print(id + 1)
        break
