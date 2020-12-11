seat_map = {}
with open('input.txt') as f:
    raw_input = f.readlines()

for y, line in enumerate(raw_input):
    for x, char in enumerate(line.strip()):
        seat_map[(x, y)] = char


xmax = len(raw_input[0].strip())
ymax = len(raw_input)


def print_map(map_):
    for x_ in range(xmax):
        for y_ in range(ymax):
            print(map_[(x_, y_)], end='')
        print('')


def iterate(map_):
    def is_occupied_int(x_, y_):
        return int(map_.get((x_, y_), ' ') == '#')

    new_map = {}
    changes = False
    for x in range(xmax):
        for y in range(ymax):
            neighbors = is_occupied_int(x - 1, y - 1) + is_occupied_int(x, y - 1) + is_occupied_int(x + 1, y - 1) \
                        + is_occupied_int(x - 1, y) + is_occupied_int(x + 1, y) \
                        + is_occupied_int(x - 1, y + 1) + is_occupied_int(x, y + 1) + is_occupied_int(x + 1, y + 1)
            if map_[(x, y)] == 'L' and neighbors == 0:
                new_map[(x, y)] = '#'
                changes = True
            elif map_[(x, y)] == '#' and neighbors >= 4:
                new_map[(x, y)] = 'L'
                changes = True
            else:
                new_map[(x, y)] = map_[(x, y)]
    return new_map, changes


while True:
    seat_map, changes = iterate(seat_map)
    if not changes:
        break

print(list(seat_map.values()).count('#'))
