"""day n"""

# common imports
import fractions
import itertools
import numpy as np
import re

with open("input") as f:
    inp = []
    for line in f.read().splitlines():
        l, r = line.split(" @ ")
        ls = tuple(map(int, l.split(", ")))
        rs = tuple(map(int, r.split(", ")))
        inp.append((ls, rs))

res = 0
for (pa, va), (pb, vb) in itertools.combinations(inp, 2):
    p1 = np.matrix(pa[:-1]).T
    v1 = np.matrix(va[:-1]).T
    p2 = np.matrix(pb[:-1]).T
    v2 = np.matrix(vb[:-1]).T

    A = np.hstack((-v1, v2))
    b = p1 - p2
    ts, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

    if np.less_equal(ts, 0).any():
        continue

    if (n := np.linalg.norm(A @ ts - b)) > 100:
        print(n)
        continue

    pos = p1 + ts[0,0] * v1
    if not np.logical_and(np.less_equal(200000000000000, pos), np.less_equal(pos, 400000000000000)).all():
        continue
    res += 1
# part 1
print(f"part 1: {res}")

# part 2
print(f"part 2: {None}")
