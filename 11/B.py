from A import Map as MapA


class Map(MapA):
    def seat_occupied_in_direction(self, position, direction):
        x = position[0]
        y = position[1]
        while True:
            x += direction[0]
            y += direction[1]
            seat = self._map.get((x, y), ' ')
            if seat == ' ' or seat == 'L':
                return 0
            if seat == '#':
                return 1


def iterate(map_):
    new_map = Map()
    changes = False
    for ((x, y), char) in map_.items():
        neighbors = sum(int(map_.seat_occupied_in_direction((x, y), direction)) for direction in
                        [(- 1, - 1), (0, - 1), (1, - 1), (- 1, 0), (1, 0), (- 1, 1), (0, 1), (1, 1)])
        if char == 'L' and neighbors == 0:
            new_map[(x, y)] = '#'
            changes = True
        elif char == '#' and neighbors >= 5:
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
