seat_map = {}
with open('input.txt') as f:
    raw_input = f.readlines()

for y, line in enumerate(raw_input):
    for x, char in enumerate(line.strip()):
        seat_map[(x, y)] = char

xmax = len(raw_input[0].strip())
ymax = len(raw_input)


def print_map(map_):
    for y_ in range(ymax):
        for x_ in range(xmax):
            print(map_[(x_, y_)], end='')
        print('')


print_map(seat_map)


def iterate(map_):
    def is_occupied_int(deltax, deltay):
        x_ = x
        y_ = y
        while True:
            x_ += deltax
            y_ += deltay
            seat = map_.get((x_, y_), ' ')
            if seat == ' ' or seat == 'L':
                return 0
            if seat == '#':
                return 1

    new_map = {}
    neighbor_map = {}
    changes = False
    for x in range(xmax):
        for y in range(ymax):
            neighbors = is_occupied_int(- 1, - 1) + is_occupied_int(0, - 1) + is_occupied_int(1, -1) \
                        + is_occupied_int(- 1, 0) + is_occupied_int(1, 0) \
                        + is_occupied_int(- 1, 1) + is_occupied_int(0, 1) + is_occupied_int(1, 1)
            neighbor_map[(x, y)] = '.' if map_[(x, y)] == '.' else neighbors
            if map_[(x, y)] == 'L' and neighbors == 0:
                new_map[(x, y)] = '#'
                changes = True
            elif map_[(x, y)] == '#' and neighbors >= 5:
                new_map[(x, y)] = 'L'
                changes = True
            else:
                new_map[(x, y)] = map_[(x, y)]

    print_map(neighbor_map)
    return new_map, changes


while True:
    seat_map, changes = iterate(seat_map)
    print_map(seat_map)
    print('')
    if not changes:
        break

print(list(seat_map.values()).count('#'))
