"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read()

inpl = []
inpl2 = []
for l in inp.splitlines():
    m = re.match(r"([UDLR]) (\d+) \(#([a-f0-9]{6})\)", l)
    assert m is not None
    (dir_, n, col) = m.groups()
    inpl.append((dir_, int(n)))
    inpl2.append(
        ({"0": "R", "1": "D", "2": "L", "3": "U"}[col[-1]], int(col[:-1], base=16))
    )

LARGE = 10**100

# part 1
# Tracing out the edge and some bounds
ub = -LARGE
db = LARGE
lb = LARGE
rb = -LARGE

cx = 0
cy = 0
edge = {(0, 0)}

for dir_, n in inpl:
    if dir_ == "U":
        for i in range(n):
            cy += 1
            edge.add((cx, cy - 1))
        ub = max(ub, cy)
    elif dir_ == "D":
        for i in range(n):
            cy -= 1
            edge.add((cx, cy + 1))
        db = min(db, cy)
    elif dir_ == "L":
        for i in range(n):
            cx -= 1
            edge.add((cx + 1, cy))
        lb = min(lb, cx)
    elif dir_ == "R":
        for i in range(n):
            cx += 1
            edge.add((cx - 1, cy))
        rb = max(rb, cx)
    else:
        assert False


# Marking out the interior using raycasting
def find_interior(edge, db, ub, lb, rb):
    interior = edge.copy()

    for j in range(db, ub + 1):
        dire = None
        inside = False
        for i in range(lb - 1, rb + 2):
            if (i, j) not in edge and (i + 1, j) in edge:
                match ((i + 1, j + 1) in edge, (i + 1, j - 1) in edge):
                    case (True, False):
                        dire = True
                    case (False, True):
                        dire = False
                    case (True, True):
                        ...
                    case (False, False):
                        assert False
            if (i, j) in edge and (i + 1, j) not in edge:
                match ((i, j + 1) in edge, (i, j - 1) in edge):
                    case (True, False):
                        inside = inside == dire
                    case (False, True):
                        inside = inside != dire
                    case (True, True):
                        inside = not inside
                    case (False, False):
                        assert False
            if inside:
                interior.add((i, j))
    return interior


print(f"part 1: {len(find_interior(edge, db, ub, lb, rb))}")

# part 2
# Finding the values at which something happens
cx = 0
cy = 0
xs = {0}
ys = {0}

for dir_, n in inpl2:
    if dir_ == "U":
        cy += n
        ys.add(cy)
    elif dir_ == "D":
        cy -= n
        ys.add(cy)
    elif dir_ == "L":
        cx -= n
        xs.add(cx)
    elif dir_ == "R":
        cx += n
        xs.add(cx)
    else:
        assert False

xsl = list(xs)
ysl = list(ys)
xsl.sort()
ysl.sort()

cx = 0
cy = 0

ci = 2 * xsl.index(0)
cj = 2 * ysl.index(0)
edge = set()

for dir_, n in inpl2:
    if dir_ == "U":
        cy += n
        while ysl[cj // 2] < cy or cj % 2:
            cj += 1
            edge.add((ci, cj - 1))
    elif dir_ == "D":
        cy -= n
        while ysl[cj // 2] > cy or cj % 2:
            cj -= 1
            edge.add((ci, cj + 1))
    elif dir_ == "L":
        cx -= n
        while xsl[ci // 2] > cx or ci % 2:
            ci -= 1
            edge.add((ci + 1, cj))
    elif dir_ == "R":
        cx += n
        while xsl[ci // 2] < cx or ci % 2:
            ci += 1
            edge.add((ci - 1, cj))
    else:
        assert False


interior = find_interior(edge, 0, 2 * len(ysl), 0, 2 * len(xsl))

total = 0
for x, y in interior:
    w = xsl[x // 2 + 1] - xsl[x // 2] - 1 if x % 2 else 1
    h = ysl[y // 2 + 1] - ysl[y // 2] - 1 if y % 2 else 1
    total += w * h

print(f"part 2: {total}")
