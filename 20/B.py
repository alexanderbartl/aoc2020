import re
from A import corners
from pprint import pprint


def count_monsters_oriented(lines):
    count = 0
    for i, line in enumerate(lines):
        for match in re.finditer('#(.{4}##){3}#', line):
            if lines[i - 1][match.start() + 18] == lines[i + 1][match.start() + 1] == lines[i + 1][match.start() + 4] == lines[i + 1][match.start() + 7] == lines[i + 1][match.start() + 10] == lines[i + 1][match.start() + 13] == lines[i + 1][match.start() + 16] == '#':
                count += 1

    return count


def count_monsters(lines):
    for i in range(8):
        monsters = count_monsters_oriented(lines)
        if monsters:
            return monsters
        # turn 90 degrees
        lines = [''.join(x) for x in zip(*lines[::-1])]
        # flip horizontally
        if i == 3:
            lines = lines[::-1]
    return None


def full_image(ordered_tiles):
    tile_rows = [
        '\n'.join([''.join(l) for row in ordered_tiles for l in zip(*(t.borderless for t in row))])
    ]
    return '\n'.join(tile_rows)


tile = corners[0]
# orient the first corner to be the top right corner
while tile.get_next('right') is None or tile.get_next('bottom') is None:
    tile.rotate()

tile_order = []
while tile:
    print('new row starting with', tile)
    tile_order.append([tile])
    tile = tile.get_next('right')
    while tile:
        # orient
        i = 0
        while tile_order[-1][-1].fingerprint_right() != tile.fingerprint_left():
            tile.rotate()
            if i == 3:
                tile.flip()
            i += 1
        tile_order[-1].append(tile)
        tile = tile.get_next('right')
    tile = tile_order[-1][0].get_next('bottom')
    if not tile:
        break
    # orient
    i = 0
    while tile_order[-1][0].fingerprint_bottom() != tile.fingerprint_top():
        tile.rotate()
        if i == 3:
            tile.flip()
        i += 1

image = full_image(tile_order)
print(image.count('#') - 15 * count_monsters(image.split('\n')))
