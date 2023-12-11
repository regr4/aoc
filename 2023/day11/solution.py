"""day n"""

# common imports
import itertools
import re

with open("input") as f:
    inp = f.read().splitlines()

n = len(inp)
m = len(inp[0])

galaxies = set()
for i, line in enumerate(inp):
    for j, ch in enumerate(line):
        if ch == "#":
            galaxies.add((i, j))


row_off = []
col_off = []

crof = 0
for i in range(n):
    if all(x != i for (x, y) in galaxies):
        crof += 1
    row_off.append(crof)

ccof = 0
for j in range(m):
    if all(y != j for (x, y) in galaxies):
        ccof += 1
    col_off.append(ccof)


expanded_galaxies_part1 = {(i + row_off[i], j + col_off[j]) for (i, j) in galaxies}
expanded_galaxies_part2 = {
    (i + 999999 * row_off[i], j + 999999 * col_off[j]) for (i, j) in galaxies
}


res1 = 0
for (x1, y1), (x2, y2) in itertools.combinations(expanded_galaxies_part1, 2):
    res1 += abs(y1 - y2) + abs(x1 - x2)

res2 = 0
for (x1, y1), (x2, y2) in itertools.combinations(expanded_galaxies_part2, 2):
    res2 += abs(y1 - y2) + abs(x1 - x2)


# part 1
print(f"part 1: {res1}")

# part 2
print(f"part 2: {res2}")
