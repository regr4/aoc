"""day n"""

from copy import deepcopy
import itertools
from operator import add
from pprint import pprint
import re

with open("input") as f:
    inp = [[int(c) for c in l] for l in f.read().splitlines()]

# part 1
w = len(inp[0])
h = len(inp)


def ib(tile):
    i, j = tile
    return 0 <= i < w and 0 <= j < h


def itr():
    for j in range(h):
        for i in range(w):
            yield (i, j)


def ix(grid, tile):
    i, j = tile
    return grid[j][i]


def orths(dirv):
    return (tuple(reversed(dirv)), tuple(map(lambda x: -x, reversed(dirv))))


# Try something like dynamic programming?

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

LARGE = 2**100
grids = {
    UP: [[LARGE for i in range(w)] for j in range(h)],
    DOWN: [[LARGE for i in range(w)] for j in range(h)],
    LEFT: [[LARGE for i in range(w)] for j in range(h)],
    RIGHT: [[LARGE for i in range(w)] for j in range(h)],
}

grids[UP][-1][-1] = inp[-1][-1]
grids[RIGHT][-1][-1] = inp[-1][-1]
grids[LEFT][-1][-1] = inp[-1][-1]
grids[DOWN][-1][-1] = inp[-1][-1]


while True:
    newgrids = deepcopy(grids)

    for di, grid in newgrids.items():
        for tile in itr():
            wt = 0
            for l in range(1, 4):
                newp = tuple(map(lambda x, y: x + l * y, tile, di))
                if not ib(newp):
                    break
                wt += ix(inp, newp)
                grid[tile[1]][tile[0]] = min(
                    ix(grid, tile), *(wt + ix(grids[o], newp) for o in orths(di))
                )

    if grids == newgrids:
        break
    grids = newgrids

res = min(x[0][0] for x in grids.values()) - inp[-1][-1]


print(f"part 1: {res}")

# part 2
print(f"part 2: {None}")
