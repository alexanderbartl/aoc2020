from collections import Counter
from re import finditer

with open('input.txt') as f:
    rules = dict(line.split(' bags contain ') for line in f.readlines())

bag_count = Counter()


def count_bags(color):
    if bag_count[color]:
        return bag_count[color]

    count = 1
    if 'no other bags' not in rules[color]:
        for match in finditer('(\d+) ([a-z]+ [a-z]+) bag', rules[color]):
            child_count, child_color = match.group(1, 2)
            count += int(child_count) * count_bags(child_color)

    bag_count[color] = count
    return count


print(count_bags('shiny gold') - 1)  # the shiny gold bag is not contained in itself
