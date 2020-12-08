with open('input.txt') as f:
    instructions = f.readlines()

idx = 0
accumulator = 0
visited = set()
while True:
    if idx in visited:
        print(accumulator)
        break
    visited.add(idx)

    if instructions[idx].startswith('nop'):
        idx += 1
    elif instructions[idx].startswith('acc'):
        accumulator += int(instructions[idx].replace('acc', '').strip())
        idx += 1
    elif instructions[idx].startswith('jmp'):
        idx += int(instructions[idx].replace('jmp', '').strip())
