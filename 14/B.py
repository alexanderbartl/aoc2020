import re

with open('input.txt') as f:
    instructions = f.readlines()


def apply_mask(mask, number):
    number_binary = format(number, '036b')
    return ''.join([number_binary[i] if masked_bit == '0' else masked_bit for i, masked_bit in enumerate(mask)])


def replace_next_x(addresses):
    with_0 = [a.replace('X', '0', 1) for a in addresses]
    with_1 = [a.replace('X', '1', 1) for a in addresses]
    return with_0 + with_1


def get_memory_addresses(mask, initial_address):
    addresses = [apply_mask(mask, initial_address)]
    while 'X' in addresses[0]:
        addresses = replace_next_x(addresses)
    return addresses


current_mask = '0' * 36
mem = {}
for instruction in instructions:
    if instruction.startswith('mask'):
        current_mask = instruction.replace('mask = ', '')
        continue

    match = re.match('mem\[(\d+)] = (\d+)', instruction)
    for address in get_memory_addresses(current_mask, int(match.group(1))):
        mem[address] = int(match.group(2))

print(sum(mem.values()))
