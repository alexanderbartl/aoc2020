with open('input.txt') as f:
    earliest = int(f.readline().strip())
    bus_ids = [int(bus) for bus in f.readline().strip().split(',') if bus != 'x']

wait_times = [(bus - earliest % bus) for bus in bus_ids]
next_bus_index = wait_times.index(min(wait_times))

print(bus_ids[next_bus_index] * (bus_ids[next_bus_index] - earliest % bus_ids[next_bus_index]))
