with open('input.txt') as f:
    f.readline()
    bus_ids = [int(bus) if bus != 'x' else None for bus in f.readline().strip().split(',')]


def find_time(busses):
    if len(busses) == 1:
        return 0, busses[0] or 1

    earliest, repeat_every = find_time(busses[:-1])
    offset = len(busses) - 1

    if busses[-1] is None:
        return earliest, repeat_every

    while (earliest + offset) % busses[-1] != 0:
        earliest += repeat_every
    return earliest, repeat_every * busses[-1]


print(find_time(bus_ids)[0])
