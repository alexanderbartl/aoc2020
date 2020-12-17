from collections import defaultdict

cubes = defaultdict(lambda: '.')
with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line):
            cubes[(x, y, 0)] = char
input_size = (x, y)


for cycle in range(1, 7):
    print(cycle)
    new_cubes = defaultdict(lambda: '.')
    for z in range(-cycle, cycle + 1):
        for y in range(-cycle, input_size[1] + cycle + 1):
            for x in range(-cycle, input_size[0] + cycle + 1):
                neighbors = [char for pos, char in cubes.items()
                             if x - 1 <= pos[0] <= x + 1 and y - 1 <= pos[1] <= y + 1 and z - 1 <= pos[2] <= z + 1
                             ].count('#') - int(cubes[(x, y, z)] == '#')

                if cubes[(x, y, z)] == '#' and 2 <= neighbors <= 3:
                    new_cubes[(x, y, z)] = '#'
                elif cubes[(x, y, z)] == '.' and neighbors == 3:
                    new_cubes[(x, y, z)] = '#'
    cubes = new_cubes

print(list(cubes.values()).count('#'))
