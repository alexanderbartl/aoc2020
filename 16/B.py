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


rule_candidates = defaultdict(list)
pos_candidates = defaultdict(list)
solutions = {}

for pos in range(len(valid_tickets[0])):
    for field, *rule in rules:
        if all([number_fits_rule(ticket[pos], *rule) for ticket in valid_tickets]):
            rule_candidates[field].append(pos)
            pos_candidates[pos].append(field)

while rule_candidates:
    for rule, positions in list(rule_candidates.items()):
        if len(positions) == 1:
            solutions[rule] = positions[0]
            del rule_candidates[rule]
            for other_rule, other_position_candidates in rule_candidates.items():
                rule_candidates[other_rule] = [pos for pos in other_position_candidates if pos != positions[0]]
            del pos_candidates[positions[0]]
            for pos, rules in pos_candidates.items():
                pos_candidates[pos] = [other_rule for other_rule in rules if other_rule != rule]

    for pos, rules in list(pos_candidates.items()):
        if len(rules) == 1:
            solutions[rules[0]] = pos
            del rule_candidates[rules[0]]
            for other_rule, other_position_candidates in rule_candidates.items():
                rule_candidates[other_rule] = [position for position in other_position_candidates if position != pos]
            del pos_candidates[pos]
            for other_pos, other_rules in pos_candidates.items():
                pos_candidates[other_pos] = [other_rule for other_rule in other_rules if other_rule != rules[0]]

final_answer = 1
for field, pos in solutions.items():
    if field.startswith('departure'):
        final_answer *= tickets[0][pos]
print(final_answer)
