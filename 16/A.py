import re

with open('input.txt') as f:
    raw = f.read()


header, nearbys = raw.split('nearby tickets:\n')
ranges = [(int(range_match.group(1)), int(range_match.group(2)))
          for range_match in re.finditer('(\d+)-(\d+)', header)]


def value_valid(value):
    for lower, upper in ranges:
        if lower <= value <= upper:
            return True
    return False


invalid_sum = 0
for value in [int(x) for nearby_ticket in nearbys.split('\n') for x in nearby_ticket.split(',') if x]:
    if not value_valid(value):
        invalid_sum += value

print(invalid_sum)