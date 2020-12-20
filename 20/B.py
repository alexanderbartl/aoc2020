import re


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


with open('example2.txt') as f:
    raw = f.read()
print(raw.count('#') - 15 * count_monsters(raw.strip().split('\n')))
