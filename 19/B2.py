import re

with open('input.txt') as f:
    rules, messages = f.read().split('\n\n')
rules = {line.split(': ')[0]: line.split(': ')[1].replace('"', '') for line in rules.split('\n')}
messages = messages.split('\n')

regexp = '(42) (42)+ (31)+'
while re.search('\d', regexp):
    regexp = re.sub('\d+', lambda match: f'({rules[match.group()]})', regexp)

regexp = re.compile(f'^{regexp.replace(" ", "")}$')
print(regexp)
print(len([message for message in messages if re.match(regexp, message)]))
