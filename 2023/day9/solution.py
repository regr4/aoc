"""day n"""

# common imports
import itertools
import re

with open("input") as f:
    inp = f.read().splitlines()

res1 = 0
res2 = 0
for line in inp:
    ns = [int(x) for x in line.split()]
    k = [ns]
    while True:
        if all(x == 0 for x in k[-1]):
            break
        k.append([])
        for a, b in itertools.pairwise(k[-2]):
            k[-1].append(b - a)

    res1 += sum(l[-1] for l in k)
    res2 += sum(l[0] * (1 - 2 * (i % 2)) for i, l in enumerate(k))

# part 1
print(f"part 1: {res1}")

# part 2
print(f"part 2: {res2}")
