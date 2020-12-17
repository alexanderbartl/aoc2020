from collections import defaultdict

cubes = defaultdict(lambda: '.')
with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line):
            cubes[(x, y, 0, 0)] = char
input_size = (x, y)


def is_neighbor(pos, x, y, z, w):
    return x - 1 <= pos[0] <= x + 1 and y - 1 <= pos[1] <= y + 1 and z - 1 <= pos[2] <= z + 1 and w - 1 <= pos[3] <= w + 1


for cycle in range(1, 7):
    print(cycle)
    new_cubes = defaultdict(lambda: '.')
    for w in range(-cycle, cycle + 1):
        for z in range(-cycle, cycle + 1):
            for y in range(-cycle, input_size[1] + cycle + 1):
                for x in range(-cycle, input_size[0] + cycle + 1):
                    neighbors = [char for pos, char in cubes.items() if is_neighbor(pos, x, y, z, w)].count('#') - \
                                int(cubes[(x, y, z, w)] == '#')

                    if cubes[(x, y, z, w)] == '#' and 2 <= neighbors <= 3:
                        new_cubes[(x, y, z, w)] = '#'
                    elif cubes[(x, y, z, w)] == '.' and neighbors == 3:
                        new_cubes[(x, y, z, w)] = '#'
    cubes = new_cubes

print(list(cubes.values()).count('#'))
