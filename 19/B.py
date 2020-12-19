import re

with open('input.txt') as f:
    rules, messages = f.read().split('\n\n')
rules = {line.split(': ')[0]: line.split(': ')[1].replace('"', '') for line in rules.split('\n')}
messages = messages.split('\n')


def evaluate_rule(rule):
    regexp = rules[rule]
    while re.search('\d', regexp):
        regexp = re.sub('\d+', lambda match: f'({rules[match.group()]})', regexp)
    regexp = regexp.replace(" ", "")
    while re.search('\([ab]+\)', regexp):
        regexp = re.sub('\(([ab]+)\)', lambda match: match.group(1), regexp)
    return regexp


def match_rule0(message):
    # rule 0 = 8 11 = 42+ 42{n}31{n} with n>0 unknown
    for i in range(1, 20):
        if re.match(f"^({rule42})+{rule42 * i}{rule31 * i}$".replace(' ', ''), message):
            return True
    return False


rule42 = f"({evaluate_rule('42')})"
rule31 = f"({evaluate_rule('31')})"
print(len([message for message in messages if match_rule0(message)]))
