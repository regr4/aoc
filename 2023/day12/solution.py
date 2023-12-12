"""day n"""

# common imports
import functools
import re

with open("input") as f:
    inp = f.read().splitlines()


@functools.lru_cache(maxsize=1000)
def solve(l: str, ns: tuple[int, ...]):
    if not ns:
        return 1 if all(x in ".?" for x in l) else 0
    if not l:
        return 0
    res = 0
    n = ns[0]
    if len(l) >= n and all(x in "#?" for x in l[:n]) and (len(l) == n or l[n] in ".?"):
        res += solve(l[n + 1 :], ns[1:])
    if l[0] in ".?":
        res += solve(l[1:], ns)
    return res


ans1 = 0
ans2 = 0
for line in inp:
    l, r = line.split()
    ns = tuple(int(x) for x in r.split(","))
    ans1 += solve(l, ns)
    ans2 += solve("?".join([l] * 5), ns * 5)


# part 1
print(f"part 1: {ans1}")

# part 2
print(f"part 2: {ans2}")
