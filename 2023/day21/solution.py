"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read().splitlines()

# part 1
n = 64

for lc,line in enumerate(inp):
    try:
        start = (lc,line.index('S'))
    except ValueError:
        pass

print(inp)
print(start)

tovisit = set([start])

visited = tovisit.copy()
for i in range(n):
    ntovisit = set()
    for y,x in tovisit:
        for ny,nx in ((y-1,x), (y+1,x),(y,x-1),(y,x+1)):
            try:
                c = inp[ny][nx]
                if c == "#" or c in visited:
                    continue
                visited.add((ny, nx))
                ntovisit.add((ny,nx))
            except IndexError:
                pass
    tovisit = ntovisit

total = 0
for pos in visited:
    if (sum(start)+sum(pos)) % 2 == n % 2:
        total += 1

print(f"part 1: {total}")

# part 2
print(f"part 2: {None}")
