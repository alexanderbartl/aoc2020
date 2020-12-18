from math import prod
import re


def calculate_without_brackets(calculation):
    while '+' in calculation:
        calculation = re.sub('(\d+) \+ (\d+)', lambda match: str(int(match.group(1)) + int(match.group(2))), calculation)
    return prod(int(term) for term in calculation.split() if term != '*')


def calculate_full(calculation):
    while '(' in calculation:
        calculation = re.sub('\(([^()]*)\)', lambda match: str(calculate_without_brackets(match.group(1))), calculation)
    return calculate_without_brackets(calculation)


with open('input.txt') as f:
    print(sum(calculate_full(line) for line in f.readlines()))
