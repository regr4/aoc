"""day n"""

from copy import deepcopy

with open("input") as f:
    inp = [[int(c) for c in l] for l in f.read().splitlines()]

w = len(inp[0])
h = len(inp)


def tiles():
    for j in range(h):
        for i in range(w):
            yield (i, j)


HORI = (1, 0)
VERT = (0, 1)

LARGE = 2**20


def solve(lo, hi):
    grids = {
        HORI: [[LARGE for i in range(w)] for j in range(h)],
        VERT: [[LARGE for i in range(w)] for j in range(h)],
    }
    grids[HORI][-1][-1] = grids[VERT][-1][-1] = 0

    while True:
        # Maybe: only check those that could possibly be affected
        # (iterate over affected and adjust any ones that need it)
        affected = set()

        for di, grid in grids.items():
            for tile in tiles():
                for m in (1, -1):
                    wt = 0
                    for l in range(1, hi):
                        newp = (tile[0] + m * l * di[0], tile[1] + m * l * di[1])
                        if not (0 <= newp[0] < w and 0 <= newp[1] < h):
                            break
                        wt += inp[newp[1]][newp[0]]
                        if l < lo:
                            continue
                        if (oth := wt + grids[(di[1], di[0])][newp[1]][newp[0]]) < (
                            grid[tile[1]][tile[0]]
                        ):
                            grid[tile[1]][tile[0]] = oth
                            affected.add((tile, di))
        if not affected:
            break
    return grids


# part 1
res = min(x[0][0] for x in solve(1, 4).values())
print(f"part 1: {res}")

# part 2
res2 = min(x[0][0] for x in solve(4, 11).values())
print(f"part 2: {res2}")
