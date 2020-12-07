with open('input.txt') as f:
    rules = [line.split(' bags contain ') for line in f.readlines()]


def find_containers(color):
    containers = []
    for container, contents in rules:
        if color in contents:
            containers.append(container)

    return containers


colors = find_containers('shiny gold')
i = 0
while i < len(colors):
    colors.extend(color for color in find_containers(colors[i]) if color not in colors)
    i += 1
print(len(colors))
