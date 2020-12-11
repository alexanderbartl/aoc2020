class Map:
    def __init__(self):
        self._map = {}

    def __getitem__(self, item):
        return self._map.get(item)

    def __setitem__(self, key, value):
        self._map[key] = value

    @classmethod
    def read_from_file(cls, filename):
        with open(filename) as f:
            raw_input = f.readlines()

        new_map = cls()

        for y, line in enumerate(raw_input):
            for x, char in enumerate(line.strip()):
                new_map[(x, y)] = char

        return new_map

    def items(self):
        return self._map.items()

    def seat_occupied(self, x, y):
        return self._map.get((x, y), ' ') == '#'

    def print(self):
        xmax = max(pos[0] for pos in self._map.keys())
        ymax = max(pos[1] for pos in self._map.keys())
        for x_ in range(xmax):
            for y_ in range(ymax):
                print(self._map[(x_, y_)], end='')
            print('')
        print('')

    def total_seats_occupied(self):
        return list(self._map.values()).count('#')


def iterate(map_):
    new_map = Map()
    changes = False
    for ((x, y), char) in map_.items():
        neighbors = sum(int(map_.seat_occupied(*pos)) for pos in
                        [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1),
                         (x, y + 1), (x + 1, y + 1)])
        if char == 'L' and neighbors == 0:
            new_map[(x, y)] = '#'
            changes = True
        elif char == '#' and neighbors >= 4:
            new_map[(x, y)] = 'L'
            changes = True
        else:
            new_map[(x, y)] = map_[(x, y)]
    return new_map, changes


if __name__ == '__main__':
    seat_map = Map.read_from_file('input.txt')
    while True:
        seat_map, has_changes = iterate(seat_map)
        if not has_changes:
            break

    print(seat_map.total_seats_occupied())
