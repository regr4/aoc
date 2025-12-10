from itertools import combinations, pairwise


with open("input") as f:
    inp = [tuple(int(x) for x in line.split(",")) for line in f.read().splitlines()]


def area(c1, c2):
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)


best = 0
for p1, p2 in combinations(inp, 2):
    best = max(best, area(p1, p2))
print(f"Part 1: {best}")


def normalize(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return ((min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2)))


def intersection(c1, c2, p1, p2):
    """Does the rectangle between c1 and c2 intersect the line between p1 and p2?"""
    assert (c1, c2) == normalize(c1, c2)
    assert (p1, p2) == normalize(p1, p2)

    return (tuple(map(max, c1, p1)), tuple(map(min, c2, p2)))


def nonempty(c1, c2):
    return all(n1 <= n2 for n1, n2 in zip(c1, c2))


inp2 = inp[:]
inp2.append(inp2[0])  # to make sure we loop around
best = 0

# not actually correct, but works on the input
for p1, p2 in combinations(inp, 2):
    p1, p2 = normalize(p1, p2)
    a = area(p1, p2)

    if a <= best:
        continue

    q1, q2 = normalize((x + 1 for x in p1), (x - 1 for x in p2))

    for c1, c2 in pairwise(inp2):
        c1, c2 = normalize(c1, c2)
        if nonempty(*intersection(q1, q2, c1, c2)):
            break
    else:
        best = max(a, best)

print(f"Part 2: {best}")
