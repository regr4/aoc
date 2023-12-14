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
for t, d in races:
    wtw = 0
    for i in range(t):
        if i * (t - i) > d:
            wtw += 1
    res *= wtw

print(f"part 1: {res}")

# part 2

# Bruteforce, but if it runs in a few seconds I'm satisfied.
t = int("".join(filter(str.isdigit, inp[0])))
d = int("".join(filter(str.isdigit, inp[1])))
wtw = 0
for i in range(t):
    if i * (t - i) > d:
        wtw += 1

print(f"part 2: {wtw}")
