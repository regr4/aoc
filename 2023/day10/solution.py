"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read().splitlines()

m = len(inp)
n = len(inp[0])
graph = {(i, j): set() for i in range(m) for j in range(n)}

CONNECTS_N = set("|LJS")
CONNECTS_S = set("|7FS")
CONNECTS_E = set("-LFS")
CONNECTS_W = set("-7JS")

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


def vadd(x, y):
    return tuple(map(lambda u, v: u + v, x, y))


def in_bounds(t):
    x, y = t
    return 0 <= x < m and 0 <= y < n


for i, line in enumerate(inp):
    for j, ch in enumerate(line):
        if (
            ch in CONNECTS_N
            and in_bounds(neigh := vadd(NORTH, (i, j)))
            and inp[neigh[0]][neigh[1]] in CONNECTS_S
        ):
            graph[(i, j)].add(neigh)
        if (
            ch in CONNECTS_S
            and in_bounds(neigh := vadd(SOUTH, (i, j)))
            and inp[neigh[0]][neigh[1]] in CONNECTS_N
        ):
            graph[(i, j)].add(neigh)
        if (
            ch in CONNECTS_E
            and in_bounds(neigh := vadd(EAST, (i, j)))
            and inp[neigh[0]][neigh[1]] in CONNECTS_W
        ):
            graph[(i, j)].add(neigh)
        if (
            ch in CONNECTS_W
            and in_bounds(neigh := vadd(WEST, (i, j)))
            and inp[neigh[0]][neigh[1]] in CONNECTS_E
        ):
            graph[(i, j)].add(neigh)
        if ch == "S":
            start = (i, j)

curr = start
loop = set()
counter = 0
while True:
    counter += 1
    for neigh in graph[curr]:
        if neigh not in loop:
            break
    else:  # wow, a for-else
        break
    loop.add(neigh)
    curr = neigh

# part 1
print(f"part 1: {counter//2}")


def ctn(pos):
    return vadd(pos, NORTH) in graph[pos]


def cts(pos):
    return vadd(pos, SOUTH) in graph[pos]


def ctw(pos):
    return vadd(pos, WEST) in graph[pos]


num_inside = 0
for point in graph.keys():
    if point in loop:
        continue

    # march to the left until we reach the edge. keep track of the number of crossings. if it's odd, we're inside the loop.
    curr = point
    ncross = 0
    while True:
        curr = vadd(curr, WEST)
        if curr[1] < 0:
            break
        if curr not in loop:
            continue
        if ctn(curr) and cts(curr):
            ncross += 1
        elif ctn(curr):
            while ctw(curr):
                curr = vadd(curr, WEST)
            if cts(curr):
                ncross += 1
        elif cts(curr):
            while ctw(curr):
                curr = vadd(curr, WEST)
            if ctn(curr):
                ncross += 1
        else:
            assert False
    num_inside += ncross % 2

# part 2
print(f"part 2: {num_inside}")
