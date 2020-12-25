public_keys = [19774466, 7290641]


def transform(value, subject_number):
    return (value * subject_number) % 20201227


def find_loop_size():
    values = [1, 1]
    for loop_size in range(1, 100_000_000):
        for x in [0, 1]:
            values[x] = transform(values[x], 7)
            if values[x] == public_keys[x]:
                return loop_size, x


loops, device = find_loop_size()
encryption_key = 1
for _ in range(loops):
    encryption_key = transform(encryption_key, public_keys[1 - device])

print(encryption_key)
