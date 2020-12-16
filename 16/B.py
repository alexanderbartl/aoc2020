import re
from collections import defaultdict

with open('input.txt') as f:
    raw = f.read()

header, nearbys = raw.split('\n\nnearby tickets:\n')
rules = [(rule_match.group(1), int(rule_match.group(2)), int(rule_match.group(3)), int(rule_match.group(4)),
          int(rule_match.group(5)))
         for rule_match in re.finditer('([^:^\n]+): (\d+)-(\d+) or (\d+)-(\d+)', header)]


def ticket_valid(ticket):
    return all([any([number_fits_rule(number, *rule[1:]) for rule in rules]) for number in ticket])


def number_fits_rule(number, lower1, upper1, lower2, upper2):
    return lower1 <= number <= upper1 or lower2 <= number <= upper2


my_ticket = [int(n) for n in header.split('\n')[-1].split(',')]
tickets = [my_ticket] + [[int(n) for n in t.split(',')] for t in nearbys.split('\n')[:-1]]
valid_tickets = [ticket for ticket in tickets if ticket_valid(ticket)]


candidates = defaultdict(list)

for pos in range(len(valid_tickets[0])):
    for field, *rule in rules:
        if all([number_fits_rule(ticket[pos], *rule) for ticket in valid_tickets]):
            candidates[field].append(pos)

while any(len(positions) > 1 for positions in candidates.values()):
    for rule, positions in list(candidates.items()):
        if len(positions) == 1:
            for other_rule, other_position_candidates in candidates.items():
                if other_rule != rule:
                    candidates[other_rule] = [pos for pos in other_position_candidates if pos != positions[0]]

final_answer = 1
for field, pos in candidates.items():
    if field.startswith('departure'):
        final_answer *= tickets[0][pos[0]]
print(final_answer)
