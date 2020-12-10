with open('input.txt') as f:
    adapters = sorted([int(l) for l in f.readlines()])

differences = [min(adapters)] + [adapters[i+1] - adapters[i] for i in range(len(adapters)-1)] + [3]
print(differences.count(1) * differences.count(3))
