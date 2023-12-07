"""day n"""

# common imports
import collections
import re

with open("input") as f:
    inp = f.read()


# part 1
def get_colors(s: str):
    res = collections.defaultdict(int)
    for c in "red", "green", "blue":
        if (m := re.search("(\\d+) " + c, s)) is not None:
            res[c] = int(m[1])
    return res


id = 1
res = 0
for line in inp.splitlines():
    s = line.split(": ")[1]
    good_line = True
    for part in s.split(";"):
        cs = get_colors(part)
        if not (cs["red"] <= 12 and cs["green"] <= 13 and cs["blue"] <= 14):
            good_line = False
            break
    if good_line:
        res += id
    id += 1

print(f"part 1: {res}")

# part 2
res = 0
for line in inp.splitlines():
    s = line.split(": ")[1]
    minr = 0
    minb = 0
    ming = 0
    for part in s.split(";"):
        cs = get_colors(part)
        minr = max(minr, cs["red"])
        ming = max(ming, cs["green"])
        minb = max(minb, cs["blue"])
    res += minr * ming * minb

print(f"part 2: {res}")
