def is_neighbor(pos, x, y, z, w):
    return x - 1 <= pos[0] <= x + 1 and y - 1 <= pos[1] <= y + 1 and z - 1 <= pos[2] <= z + 1 and w - 1 <= pos[3] <= w + 1


def run(four_d=False):
    active_cubes = set()
    with open('input.txt') as f:
        for y, line in enumerate(f.readlines()):
            for x, char in enumerate(line):
                if char == '#':
                    active_cubes.add((x, y, 0, 0))
    input_size = (x, y)

    for cycle in range(1, 7):
        print(cycle)
        new_cubes = set()
        for w in [0] if not four_d else range(-cycle, cycle + 1):
            for z in range(-cycle, cycle + 1):
                for y in range(-cycle, input_size[1] + cycle + 1):
                    for x in range(-cycle, input_size[0] + cycle + 1):
                        neighbors = len([pos for pos in active_cubes if is_neighbor(pos, x, y, z, w)]) \
                                    - int((x, y, z, w) in active_cubes)

                        if (x, y, z, w) in active_cubes and 2 <= neighbors <= 3:
                            new_cubes.add((x, y, z, w))
                        elif (x, y, z, w) not in active_cubes and neighbors == 3:
                            new_cubes.add((x, y, z, w))
        active_cubes = new_cubes

    return len(active_cubes)


print(run(False))
print(run(True))
