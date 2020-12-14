import re

with open('input.txt') as f:
    instructions = f.readlines()


def apply_mask(mask, number):
    number_binary = format(number, '036b')
    masked_binary = ''.join([number_binary[i] if masked_bit == 'X' else masked_bit for i, masked_bit in enumerate(mask)])
    return int(masked_binary, 2)


current_mask = 'X' * 36
mem = {}
for instruction in instructions:
    if instruction.startswith('mask'):
        current_mask = instruction.replace('mask = ', '')
        continue

    match = re.match('mem\[(\d+)] = (\d+)', instruction)
    mem[int(match.group(1))] = apply_mask(current_mask, int(match.group(2)))

print(sum(mem.values()))
