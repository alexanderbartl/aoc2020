from A import black_tile_positions
from collections import Counter


def neighbors(pos):
    x, y = pos
    return [(x + 1, y + 1), (x + 2, y), (x + 1, y - 1), (x - 1, y - 1), (x - 2, y), (x - 1, y + 1)]


for i in range(100):
    black_neighbor_count = Counter(pos2 for pos in black_tile_positions for pos2 in neighbors(pos))
    black_tile_positions = set(pos for pos in black_tile_positions if black_neighbor_count[pos] in [1, 2]).union(
        set(pos for pos, count in black_neighbor_count.items() if count == 2 and pos not in black_tile_positions))

print(len(black_tile_positions))
