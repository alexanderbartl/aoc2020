with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

def count_trees(right, down=1):
    x = 0
    trees = 0
    for line in lines[::down]:
        trees += int(line[x] == '#')
        x = (x + right) % len(line)

    return trees

# A
print(count_trees(3))

# B
print(count_trees(1) * count_trees(3) * count_trees(5) * count_trees(7) * count_trees(1, 2))