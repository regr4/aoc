"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read().strip()

state = 50
l1 = 0
for l in inp.split("\n"):
    state += int(l[1:]) * (-1 if l[0] == "L" else 1)
    state %= 100
    if state == 0:
        l1 += 1


# inefficient but fine for the size of data.
state = 50
l2 = 0
for l in inp.split("\n"):
    direction = -1 if l[0] == "L" else 1
    magnitude = int(l[1:])
    for _ in range(magnitude):
        state += direction
        state %= 100
        if state == 0:
            l2 += 1

# part 1
print(f"part 1: {l1}")

# part 2
print(f"part 2: {l2}")
