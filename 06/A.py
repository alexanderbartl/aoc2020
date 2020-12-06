with open('input.txt') as f:
    groups = f.read().split('\n\n')

# A
print(sum([len(set(group.replace('\n', ''))) for group in groups]))

# B
count = 0
for group in groups:
    answers = [set(a) for a in group.split('\n')]
    count += len(set.intersection(*answers))
print(count)
