import re


def calculate_without_brackets(calculation):
    expressions = calculation.strip().split()
    value = int(expressions[0])
    for i in range(1, len(expressions), 2):
        operator, value2 = expressions[i], int(expressions[i + 1])
        value = value * value2 if operator == '*' else value + value2
    return value


def calculate_full(calculation):
    while '(' in calculation:
        calculation = re.sub('\(([^()]*)\)', lambda match: str(calculate_without_brackets(match.group(1))), calculation)
    return calculate_without_brackets(calculation)


with open('input.txt') as f:
    print(sum(calculate_full(line) for line in f.readlines()))
