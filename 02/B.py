from re import compile

regexp = compile('(\d+)-(\d+) (\w): (\w+)')

with open('input.txt') as f:
    matches = [regexp.match(line) for line in f.readlines()]

valid = 0
for match in matches:
    first, second, letter, password = int(match[1]), int(match[2]), match[3], match[4]
    valid += int((password[first - 1] == letter or password[second - 1] == letter )and password[first - 1] != password[second - 1])

print(valid)