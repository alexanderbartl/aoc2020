from functools import lru_cache

with open('input.txt') as f:
    adapters = sorted([int(l) for l in f.readlines()])


@lru_cache
def combinations_to_output_jolt(jolt):
    if jolt == 0:
        return 1
    if jolt not in adapters:
        return 0
    return combinations_to_output_jolt(jolt - 1) + combinations_to_output_jolt(jolt - 2) + combinations_to_output_jolt(
        jolt - 3)


print(combinations_to_output_jolt(max(adapters)))
