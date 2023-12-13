"""day n"""

# common imports
import re

with open("input") as f:
    inp = [b.splitlines() for b in f.read().split("\n\n")]


def transpose(b):
    m = len(b)
    n = len(b[0])
    return [[b[i][j] for i in range(m)] for j in range(n)]


def check_reflection(b, i):
    assert 2 * (i + 1) <= len(b)
    return b[2 * i + 1 :: -1] == b[: 2 * (i + 1)]


# duplicate :( why doesn't python have anything built-in to get
# (without removing) an arbitrary element from a set, or 0 if it's
# empty?
def solve(b):
    for i in range(len(b) // 2):
        if check_reflection(b, i):
            return i + 1
        if 2 * (i + 1) <= len(b) - 1 and check_reflection(b[-1::-1], i):
            return len(b) - i - 1
    return 0


def findall(b):
    res = set()
    for i in range(len(b) // 2):
        if check_reflection(b, i):
            res.add(i + 1)
        if 2 * (i + 1) <= len(b) - 1 and check_reflection(b[-1::-1], i):
            res.add(len(b) - i - 1)
    return res


class GotResult(Exception):
    def __init__(self, n):
        self.n = n


ans = 0
ans2 = 0
for board in inp:
    b = [[ch == "#" for ch in r] for r in board]
    r = solve(b)
    ans += 100 * r
    tr = solve(transpose(b))
    ans += tr

    try:
        for i in range(len(b)):
            for j in range(len(b[i])):
                b[i][j] = not b[i][j]
                s = findall(b) - {r}
                ts = findall(transpose(b)) - {tr}
                if s:
                    raise GotResult(100 * s.pop())
                if ts:
                    raise GotResult(ts.pop())
                b[i][j] = not b[i][j]
    except GotResult as res:
        ans2 += res.n

print(f"part 1: {ans}")

print(f"part 2: {ans2}")
