"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read().splitlines()

# part 1
def ints(s):
    return [int(x) for x in re.findall(r"-?\d+", s)]

times = ints(inp[0])
distances = ints(inp[1])

races = list(zip(times, distances))

res = 1
for race in races:
    wtw = 0
    t, d = race
    for i in range(t):
        if i*(t-i) > d:
            wtw += 1

    res *= wtw

print(f"part 1: {res}")

#part 2

# Bruteforce, but if it runs in a few seconds I'm satisfied.
newtime = int("".join(filter(str.isdigit, inp[0])))
newdistance = int("".join(filter(str.isdigit, inp[1])))

wtw = 0
t, d = newtime, newdistance
for i in range(t):
    if i*(t-i) > d:
        wtw += 1

print(f"part 2: {wtw}")
