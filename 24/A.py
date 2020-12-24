with open('input.txt') as f:
    instructions = f.readlines()

black_tile_positions = set()
for line in instructions:
    pos_x = pos_y = 0
    delta_y = 0
    for letter in line:
        if letter in 'ns':
            delta_y = 1 if letter == 'n' else -1
        else:
            delta_x = (1 if letter == 'e' else -1) * (2 if delta_y == 0 else 1)
            pos_x += delta_x
            pos_y += delta_y
            delta_y = 0

    position = pos_x, pos_y
    if position in black_tile_positions:
        black_tile_positions.remove(position)
    else:
        black_tile_positions.add(position)

print(len(black_tile_positions))
