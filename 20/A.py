import math

with open('input.txt') as f:
    raw_tiles = f.read().split('\n\n')


def fingerprint(string):
    return int(string.replace('.', '0').replace('#', '1'), 2)


def parse_tile(raw_tile):
    lines = raw_tile.strip().split('\n')
    id = int(lines[0][5:9])
    border_top = fingerprint(lines[1].strip())
    border_bottom = fingerprint(lines[10].strip())
    border_left = fingerprint(''.join(l[0] for l in lines[1:]))
    border_right = fingerprint(''.join(l[9] for l in lines[1:]))
    border_top_r = fingerprint(lines[1].strip()[::-1])
    border_bottom_r = fingerprint(lines[10].strip()[::-1])
    border_left_r = fingerprint(''.join(l[0] for l in lines[1:])[::-1])
    border_right_r = fingerprint(''.join(l[9] for l in lines[1:])[::-1])
    return id, (border_top, border_right, border_bottom, border_left, border_top_r, border_right_r, border_bottom_r, border_left_r)


def flip_fingerprint(n):
    return int(bin(n)[:1:-1], 2)


tiles = dict(parse_tile(t) for t in raw_tiles)
all_borders = [b for borders in tiles.values() for b in borders]
corners = []
for id, borders in tiles.items():
    matches = sum(all_borders.count(b) for b in borders[:4])
    if matches == 6:
        corners.append(id)

print(corners)
print(math.prod(corners))
