with open('input.txt') as f:
    original_instructions = f.readlines()


def run(instructions, replace_nth):
    instructions = instructions.copy()
    idx = 0
    accumulator = 0
    visited = set()
    while True:
        if idx in visited:
            return None
        elif idx == len(instructions):
            return accumulator

        visited.add(idx)
        if len(visited) == replace_nth + 1:
            instructions[idx] = instructions[idx].replace('nop', 'tmp').replace('jmp', 'nop').replace('tmp', 'jmp')

        if instructions[idx].startswith('nop'):
            idx += 1
        elif instructions[idx].startswith('acc'):
            accumulator += int(instructions[idx].replace('acc', '').strip())
            idx += 1
        elif instructions[idx].startswith('jmp'):
            idx += int(instructions[idx].replace('jmp', '').strip())


for n in range(len(original_instructions)):
    result = run(original_instructions, n)
    if result is not None:
        print(result)
        break
